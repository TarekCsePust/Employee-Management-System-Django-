from django.shortcuts import render,redirect,reverse,get_object_or_404,HttpResponse
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


def EmployeeList(request):
	if request.user.is_authenticated:
		employees = Employee.objects.filter(company=request.user)
		print(employees)
		return render(request,"list.html",{"employees":employees})
		return HttpResponse(employees)
	return redirect("account:login")
	
def CreateEmployee(request):
	if request.user.is_authenticated:
		form = EmployeeForm(request.POST or None,request.FILES or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.company = request.user
			instance.save()
			return redirect("employee:list")
	
		return render(request,"create.html",{"form":form})
	return redirect("account:login")

	
def EmployeeDetail(request,pk):
	if request.user.is_authenticated:
		employee = get_object_or_404(Employee,pk=pk)
		if(employee.company == request.user):
			return render(request,"detail.html",{"employee":employee})
		else:
			return redirect("employee:list")
	return redirect("account:login")

def EmployeeUpdate(request,pk):
	if request.user.is_authenticated:
		employee = get_object_or_404(Employee,pk=pk)
		if(employee.company == request.user):
			form = EmployeeForm(request.POST or None,request.FILES or None,instance=employee)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				return redirect('employee:detail', pk=employee.id)
			return render(request,"create.html",{"form":form})		
			
		else:
			return redirect("employee:list")
	return redirect("account:login")

