from django.shortcuts import render, get_object_or_404,redirect
from .models import Empolyee
from .form import EmployeeForm
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status


def viewemployee(request):
    query = request.GET.get('search')
    department = request.GET.get('department')

    employee = Empolyee.objects.all()

    if query:
        employee = employee.filter(name__icontains=query)

    if department:
        employee = employee.filter(department__icontains=department)

    return render(request, 'employeeview.html', {"employee": employee})

def employeedetails(request, id):
    employee = get_object_or_404(Empolyee, id=id)
    return render(request, 'employeedetails.html', {"employee": employee})

def addemployee(request):
    form=EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('view')
    return render(request,'addemployee.html',{'form':form})

def editemployee(request,id):
    employee=get_object_or_404(Empolyee,id=id)
    form=EmployeeForm(request.POST or None ,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('view')
    return render(request,'editemployee.html',{'form':form})





# API


class EmployeeAPIView(APIView):
    def get(self,request):
        employee=Empolyee.objects.all()
        serializer=EmployeeSerializer(employee,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeDetailsApIView(APIView):
    def get_employee(self,id):
        try:
            return Empolyee.objects.get(id=id)
        except Empolyee.DoesNotExist:
            return None
        
    def patch(self,request,id):
        empoyee=self.get_employee(id)
        if not empoyee:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=EmployeeSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
    def delete(self,request,id):
        empoyee=self.get_employee(id)
        if not empoyee:
            return Response(status=status.HTTP_404_NOT_FOUND)
        empoyee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    