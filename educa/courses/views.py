from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Course
from django.contrib.auth.mixins import LoginRequiredMixin, \
                                        PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, \
                                            DeleteView

## Inline Form
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from .forms import ModuleFormSet

class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name = 'courses/manage/module/formset.html'
    course = None

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course, data=data)

    def dispatch(self, request, pk):
        self.course = get_object_or_404(Course, id=pk, owner=request.user)
        return super(CourseModuleUpdateView, self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'course': self.course,
                                        'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('manage_course_list')
        return self.render_to_response({'course': self.course,
                                        'formset': formset})



# Owner mixins allows to define the behaviour of class
class OwnerMixin(object):
    """
    These mixins can be used with
    any models with owner attribute
    """
    def get_querysset(self):
        qs = super(OwnerMixin, self).get_querysset()
        return qs.filter(owner=self.request.user)

class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)

class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin):
    model = Course

class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')
    template_name = 'courses/manage/course/form.html'

### List view without mixins (concept)
# class ManageCourseListView(ListView):
#     model = Course
#     template_name = 'courses/manage/course/list.html'
#
#     def get_querysset(self):
#         qs = super(ManageCourseListView, self).get_querysset()
#         return qs.filter(owner=self.request.user)

#### Views
class ManageCourseListView(OwnerCourseMixin, ListView): #listview with mixin
    template_name = 'courses/manage/course/list.html'

class CourseCreateView(PermissionRequiredMixin,
                        OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.add_course'

class CourseUpdateView(PermissionRequiredMixin,
                        OwnerCourseEditMixin, UpdateView):
    permission_required = 'courses.change_course'

class CourseDeleteView(PermissionRequiredMixin,
                        OwnerCourseMixin, DeleteView):
    permission_required = 'courses.delete_course'
    template_name = 'courses/manage/course/delete.html'
    success_url = reverse_lazy('manage_course_list')
