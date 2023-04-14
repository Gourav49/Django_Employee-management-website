from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
import json
from django.http import HttpResponse
from django.core.serializers import serialize
from testapp.mixins import SerializeMixin,HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json
from testapp.forms import EmployeeForm
from django import forms

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(SerializeMixin,HttpResponseMixin,View):
    def get_object_by_id(self,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp

    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json_dumps({'msg':'Pleae enter valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            emp=self.get_object_by_id(id)
            if emp is None:
                json_data=json.dumps({'msg':'The request resource not available'})
                return self.render_to_http_response(json_data,status=404)
            json_data=self.Serialize([emp,])
            return self.render_to_http_response(json_data)
        qs=Employee.objects.all()
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)


    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Pleae enter valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        empdata=json.loads(data)
        form=EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resource Created Successfully'})
            return self.render_to_http_response(json_data)
        if form.errors():
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Pleae enter valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            emp=self.get_object_by_id(id)
        else:
            json_data=json.dumps({'msg':'To perform updation id is mandatory'})
            return self.render_to_http_response(json_data,status=404)
        if emp is None:
            json_data=json.dumps({'msg':'The requested Id has no match with available database'})
            return self.render_to_http_response(json_data,status=404)
        provided_data=json.loads(data)
        original_data={
        'eno' : emp.eno,
        'ename' : emp.ename,
        'esal' : emp.esal,
        'eaddr' : emp.eaddr,
        }
        original_data.update(provided_data)
        form=EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Updation completed Successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)


    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Pleae enter valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            emp=self.get_object_by_id(id)
        else:
            json_data=json.dumps({'msg':'To perform Deletion id is mandatory'})
            return self.render_to_http_response(json_data,status=404)
        if emp is None:
            json_data=json.dumps({'msg':'No matched data found, cannot perform deletion'})
            return self.render_to_http_response(json_data,status=404)
        status,deleted_item=emp.delete()
        if status== 1:
            json_data=json.dumps({'msg':'Resource Deleted Successfully'})
            return self.render_to_http_response(json_data)
        json_data=json.dumps({'msg':'Unable to delete....Please Try Again'})
        return self.render_to_http_response(json_data)




















# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeeDetailCBV(SerializeMixin,HttpResponseMixin,View):
#     def get_object_by_id(self,id):
#         try:
#             emp=Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#             emp=None
#         return emp
#
#     def get(self,request,id,*args,**kwargs):
#         try:
#             emp = Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#             json_data=json.dumps({'msg':'The requested resource not available'})
#             #return HttpResponse(json_data,content_type='application/json',status=404)
#             return self.render_to_http_response(json_data,status=404)
#
#         #emp_data= {
#         #'eno' : emp.eno,
#         #'ename' : emp.ename,
#         #'esal' : emp.esal,
#         #'eaddr' : emp.eaddr,
#         #}
#         #json_data=json.dumps(emp_data)
#         else:
#             json_data=self.Serialize([emp,])
#             #return HttpResponse(json_data,content_type='application/json',status=200)
#             return self.render_to_http_response(json_data)

    # def put(self,request,id,*args,**kwargs):
    #     emp=self.get_object_by_id(id)
    #     if emp is None:
    #         json_data=json.dumps({'msg':'No matched data found, cannot perform updation'})
    #         return self.render_to_http_response(json_data,status=404)
    #     data=request.body
    #     valid_json=is_json(data)
    #     if not valid_json:
    #         json_data=json.dumps({'msg':'Please provide valid json data'})
    #         return self.render_to_http_response(json_data,status=400)
    #     provided_data=json.loads(data)
    #     original_data={
    #     'eno' : emp.eno,
    #     'ename' : emp.ename,
    #     'esal' : emp.esal,
    #     'eaddr' : emp.eaddr,
    #     }
    #     original_data.update(provided_data)
    #     form=EmployeeForm(original_data,instance=emp)
    #     if form.is_valid():
    #         form.save(commit=True)
    #         json_data=json.dumps({'msg':'Updation completed Successfully'})
    #         return self.render_to_http_response(json_data)
    #     if form.errors:
    #         json_data=json.dumps(form.errors)
    #         return self.render_to_http_response(json_data,status=400)

    # def delete(self,request,id,*args,**kwargs):
    #     emp=self.get_object_by_id(id)
    #     if emp is None:
    #         json_data=json.dumps({'msg':'No matched data found, cannot perform deletion'})
    #         return self.render_to_http_response(json_data,status=404)
    #     status,deleted_item=emp.delete()
    #     if status==1:
    #         json_data=json.dumps({'msg':'Resource Deleted Successfully'})
    #         return self.render_to_http_response(json_data)
    #     json_data=json.dumps({'msg':'Unable to delete....Please Try Again'})
    #     return self.render_to_http_response(json_data)
    #

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeListCBV(SerializeMixin,HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        qs = Employee.objects.all()
        json_data=self.Serialize(qs)
        #p_data=json.loads(json_data)
        #final_list=[]
        #for obj in p_data:
            #emp_data=obj['fields']
            #final_list.append(emp_data)
        #json_data=json.dumps(final_list)
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        data =request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json_data only'})
            return self.render_to_http_response(json_data,status=400)
        #json_data=json.dumps({'msg':'You Provided a valid json data'})
        #return self.render_to_http_response(json_data)
        empdata=json.loads(data)
        form= EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resource created Successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
