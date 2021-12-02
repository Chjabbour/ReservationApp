from django.shortcuts import render
from student.models import Studentdetails, CommentData, Bookdetails, Reservationdata

from django.db import connection
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def home(request):
    mydict = {'name':'Shadi Jabbour'}
    return render(request, 'student/home.html', mydict)

@login_required
def studentdetails(request):
    studentdata = Studentdetails.objects.all()
    paginator = Paginator(studentdata, 10)
    page = request.GET.get('page')
    pagedata = paginator.get_page(page)
    context = {'data':pagedata}
    return render(request, 'student/studentdetails.html', context)

@login_required
def bookdetails(request):
    bookdata = Bookdetails.objects.all()
    paginator = Paginator(bookdata, 10)
    page = request.GET.get('page')
    pagedata = paginator.get_page(page)
    context = {'data':pagedata}
    return render(request, 'student/bookdetails.html', context)

@login_required
def commentpage(request):
    request.session['username'] = request.user.username #key value pair for user
    return render(request, 'student/comment.html')

@login_required
def savecomment(request):
    if('emailid' and 'commentid' in request.GET):
        useremail = request.GET.get('emailid')
        usercomment = request.GET.get('commentid')
        dataobj = CommentData(useremail= useremail, usercomment = usercomment)
        dataobj.save()
    return HttpResponse('Success')

# Display book details and student names. reserve a book for a student
@login_required
def reserve(request):
    studentdata = Studentdetails.objects.all()
    bookdata = Bookdetails.objects.all()
    reservation = Reservationdata.objects.all()
    context = {'student':studentdata, 'book':bookdata, 'reservation':reservation}
    return render(request, 'student/reservation.html', context)
    # reservation = Reservationdata.objects.all()
    # context = {'student':studentdata, 'book': bookdata, 'reservation': reservation}
    # return render(request, 'student/book.html', context)


def savereservation(request):
    if('StudentID' and 'BookTitle' in request.GET):
        student = request.GET.get('StudentID')
        book = request.GET.get('BookTitle')
        snum = Reservationdata.objects.filter(StudentID=student).count()
        bnum = Reservationdata.objects.filter(BookTitle=book).count()
        if snum < 3 and bnum == 0:
            dataobj = Reservationdata(StudentID=student, BookTitle=book)
            dataobj.save()
            return HttpResponse('Reserved')
        else:
            return HttpResponse('Failed Reservation')

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

@login_required
def chart(request):
    cursorobj = connection.cursor()
    cursorobj.execute("select AVG(GPA) From student_studentdetails")
    dict = cursorobj.fetchall()
    for i in dict:
        for averagegpa in i:
            print(averagegpa)
    enrolledstudents = Studentdetails.objects.count()
    seniors = Studentdetails.objects.filter(Year='Senior').count()
    juniors = Studentdetails.objects.filter(Year='Junior').count()
    sophomores = Studentdetails.objects.filter(Year='Sophomore').count()
    context = {'enrolledstudents': enrolledstudents, 'averagegpa':averagegpa, 'seniors':seniors, 'juniors':juniors, 'sophomores':sophomores, 'name':'Shadi Jabbour'}
    return render(request, 'student/chart.html', context)




# def studentdetails(request):
#     fname = 'Beth'
#     cursorobj = connection.cursor()
#     cursorobj.execute("SELECT * FROM student_studentdetails WHERE firstname = %s", [fname])
#     studentdata = dictfetchall(cursorobj)
#     print(studentdata)
#     context = {'data':studentdata}
#     return render(request, 'student/studentdetails.html', context)


# Create your views here.
