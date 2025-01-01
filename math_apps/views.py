from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'views/index.html')

def calculator(request):
    if request.method == 'POST':
        userInput = request.POST
        if 'clear' in userInput:
            request.session['history'] = []
            return render(request, 'views/calculator.html')
        else:
            try:
                operation = userInput['operation']
                num1 = userInput['num1']
                num2 = userInput['num2']

                if operation == 'add':
                    expression = num1 + '+' + num2
                elif operation == 'subtract':
                    expression = num1 + '-' + num2
                elif operation == 'multiply':
                    expression = num1 + '*' + num2
                elif operation == 'divide':
                    expression = num1 + '/' + num2
                else:
                    expression = 'Error'

                result = eval(expression)
            except:
                result = 'Error'

            history = request.session.get('history', [])
            history.insert(0, expression + ' = ' + str(result))
            request.session['history'] = history

        return render(request, 'views/calculator.html', {'history': history})
    else:
        return render(request, 'views/calculator.html', {})
