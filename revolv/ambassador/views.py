from revolv.base.utils import ProjectGroup
from revolv.base.views import BaseStaffDashboardView
from revolv.project.models import Project


class AmbassadorDashboardView(BaseStaffDashboardView):
    """Basic view for the Ambassador dashboard.
    """
    template_name = 'base/dashboard.html'
    role = "ambassador"

    def get_filter_args(self):
        """
        Return a list that contains a set of projects that this user owns, to pass
        to various Project filtering functions.
        """
        return [Project.objects.owned_projects(self.user)]

    def get_context_data(self, **kwargs):
        context = super(AmbassadorDashboardView, self).get_context_data(**kwargs)
        if self.user_profile and self.user_profile.reinvest_pool > 0.0:
            context["reinvestment_amount"] = self.user_profile.reinvest_pool
        else:
            context["reinvestment_amount"] = 0.0
        context["project_dict"][ProjectGroup('Drafted Projects', "drafted")] = Project.objects.get_drafted(*self.get_filter_args())
        return context

