from django.http import HttpResponseRedirect
from django.shortcuts import render

from chart.forms import CheckUrlForm
import subprocess

def get_url(request):
    if request.method == 'POST':
        form = CheckUrlForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = CheckUrlForm()
    return render(request, 'chart/url.html', {'form': form})


def checkVulnerability(request):
    if request.method == 'POST':
        form = CheckUrlForm(request.POST)
        if form.is_valid(): # All validation rules pass
            rohy = form.cleaned_data['url']
            pathNikto = 'C:\\Users\\Stephan\\Desktop\\program\\'
            # CSV Out
            output = 'C:\\Users\\\Stephan\\Desktop\\testNikto.csv'
            cmd = 'perl ' + pathNikto + 'nikto.pl -h ' + rohy + ' -no404 -Format csv -output ' + output
            subprocess.call(cmd, shell=True)
            # Open result file and find CVE-line number
            try:
                with open(output) as myFile:
                    for num, line in enumerate(myFile, 1):
                        if 'CVE-' in line:
                            index = line.index('CVE-')
                            cve_id = line[index:index+13]
                            break

                        else:
                            cve_id = None

                    print cve_id
            except IOError:
                pass
        return rohy
