from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import OutputImage, InputImage, TestImage,TestOutput
from django.conf import settings
import tensorflow_hub as hub
import tensorflow as tf
import cv2
import numpy as np
import random
from PIL import Image
# Create your views here.


def home(request):

    img = OutputImage.objects.values_list('result_image', flat=True).last()
    Iform = ImageForm
    context = {
        'Iform': Iform,
        'img': img,
    }
    if request.method == 'POST':
        Iform = ImageForm(request.POST, request.FILES)
        if Iform.is_valid():
            Iform.save()
            input_image = InputImage.objects.values_list().last()
            nst(input_image[1],input_image[2],1)
            return redirect('/')
    return render(request, 'home.html', context)


def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.io.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img


def nst(image1,image2,x):
    
    im=Image.open(image1)

    im.save(image1)

    hub_model = hub.load(
        'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

    style=load_image(image1)
    source=load_image(image2)
    result_image = hub_model(tf.constant(source), tf.constant(style))[0]
    filename = str(random.randint(1000, 98765431))
    
    if x==2:
        cv2.imwrite('orpage/result/'+filename+'.jpg',
                cv2.cvtColor(np.squeeze(result_image)*255, cv2.COLOR_BGR2RGB))
        output=TestOutput()
        output.out_images='orpage/result/'+filename+'.jpg'
        output.save()
    else:
        cv2.imwrite('main/files/result/'+filename+'.jpg',
                cv2.cvtColor(np.squeeze(result_image)*255, cv2.COLOR_BGR2RGB))
        output = OutputImage()
        output.result_image = 'main/files/result/'+filename+'.jpg'
        output.save()

def orpage(request):
    if request.method=='POST':
        id1=request.POST.get('test1','no')
        id2=request.POST.get('test2','no')
        image1=str(id1).replace('test', 'orpage/test')
        image2=str(id2).replace('test', 'orpage/test')
        nst(image1, image2,2)
        return redirect('orpage')
    img=TestOutput.objects.values_list('out_images',flat=True).last()
    test_img = TestImage.objects.values_list('images', flat=True)
    
    if img is None:
        img_str=None
    else:
        img_str=str(img)
        img_str=img_str.replace('orpage/', '')
    print(img)
    print(img_str)
    new_list=list()
    for i in test_img:
        s=str(i)
        s=s.replace('orpage/', '')
        new_list.append(s)
    context = {
        'test_img': new_list,
        'img': img_str,
    }
    return render(request, 'two.html', context)

def clearall(request):
    out=OutputImage.objects.all()
    inputt=InputImage.objects.all()
    out.delete()
    inputt.delete()
    return redirect('home')

def clearall2(request):
    out=TestOutput.objects.all()
    out.delete()
    return redirect('orpage')