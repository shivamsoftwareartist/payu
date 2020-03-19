from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, Template,RequestContext
import datetime
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
# from django.core.context_processors import csrf

# import urllib2
from urllib.request import urlopen
import json
from uuid import uuid4
from hashlib import sha512
import requests
from django.conf import settings
from django.http import JsonResponse



def index(request):
    return render(request, "index.html")
    

@csrf_exempt
def Home(request):
    key = settings.PAYU_MERCHANT_KEY
    salt = settings.PAYU_MERCHANT_SALT
    txnid = uuid4().hex
    amount = '1'
    firstname = 'Jaysinh'
    email = 'dummyemail@dummy.com'
    phone = '6111111111'
    productinfo = 'Bag'
    # service_provider = "payu_paisa"
    posted={}

    hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt"
    # hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt"
    posted['key']= key
    hash_string = ''
    hashVarsSeq=hashSequence.split('|')
    for i in hashVarsSeq:
        try:
            hash_string+=str(posted[i])
        except Exception:
            hash_string+=''
        hash_string+='|'
    hash_string+=str(salt)
    hashh = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
    print(hashh)
    # hashh = hashlib.sha512(hashSequence.encode('utf-8')).hexdigest().lower()
    data = {
        "key": salt,
        "txnid": txnid,
        "amount": amount,
        "productinfo": productinfo,
        "firstname": firstname,
        "email": email,
        "phone": phone,
        "surl" : 'http://127.0.0.1:8000/payment/success',
        "furl": 'http://127.0.0.1:8000/payment/failure',
        "hash": hashh,
        "service_provider": "payu_paisa",
        }
    print(data)
    url = 'https://sandboxsecure.payu.in/_payment'
    successful = requests.post(url, data=data)
    return HttpResponse(successful)
    # return HttpResponse('payment successful')





















# def Home(request):
#     key = settings.PAYU_MERCHANT_KEY
#     salt = settings.PAYU_MERCHANT_SALT
#     print('1', key, salt)
#     print(key)
#     txnid = uuid4().hex
#     print('2', txnid)
#     amount = '1'
#     firstname = 'Jaysinh'
#     email = 'dummyemail@dummy.com'
#     phone = '6111111111'
#     productinfo = 'Bag'
#     posted={}

    # hashSequence = key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt
    # hash = hash("sha512", $hashSequence);
    # udf1 = ''
    # udf2 = ''
    # udf3 = ''
    # udf4 = ''
    # udf5 = ''
    # udf6 = ''
    # udf7 = ''
    # udf8 = ''
    # udf9 = ''
    # udf10 = ''
    # hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt"
    # hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt"
    # posted['key']= key
    # hash_string = ''
    # hashVarsSeq=hashSequence.split('|')
    # for i in hashVarsSeq:
    #     try:
    #         hash_string+=str(posted[i])
    #     except Exception:
    #         hash_string+=''
    #     hash_string+='|'
    # print('3', salt)
    # hash_string+=str(salt)
    # print(hash_string)
    # hashh = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
    # print('4', hashh)
    # # hashh = hashlib.sha512(hashSequence.encode('utf-8')).hexdigest().lower()
    # data = {
    #     "key": salt,
    #     "txnid": txnid,
    #     "amount": amount,
    #     "productinfo": productinfo,
    #     "firstname": firstname,
    #     "email": email,
    #     "phone": phone,
    #     "surl" : 'http://127.0.0.1:8000/payment/success',
    #     "furl": 'http://127.0.0.1:8000/payment/failure',
    #     "hash": hashh,
    #     "service_provider": payu_paisa,
    #     }
    # print('5',data)
    # url = 'https://sandboxsecure.payu.in/_payment'

    # # $.ajax({
    # #     "url": url,
    # #     "type": "post",
    # #     "data": data
    # #    "success": success_callback,
    # #    "error": error_callback
    # # })
    
    
    # # successful = urllib2.urlopen("https://sandboxsecure.payu.in/_payment", data)
    # successful = requests.post(url, data=data)
    # print('6')
    # print(successful.text)
    # # return render(request, "index")
    # # successful = urlopen(url, data)
    # return HttpResponse(successful)
    # return HttpResponse('payment successful')


# "success_url": "http://127.0.0.1:8000/payment/success",
# "failure_url": "http://127.0.0.1:8000/payment/failure",

# surl : 'https://sucess-url.in',
# furl: 'https://fail-url.in',














@csrf_exempt
def success(request):
    return (request, "success.html")
# def payu_success(request):
#     data = dict(zip(request.POST.keys(), request.POST.values()))
#     response = payu.check_hash(data)
#     return JsonResponse(response)


# Payu failure page
@csrf_exempt
def failure(request):
    return (request, "Failure.html")
# def payu_failure(request):
#     data = dict(zip(request.POST.keys(), request.POST.values()))
#     response = payu.check_hash(data)
#     return JsonResponse(response) 
