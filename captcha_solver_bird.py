from cv2 import randn
import requests
import base64
import threading
import os
import time
import random
from IPython.display import clear_output


from PIL import Image
from io import BytesIO
import checkbird
import detect_recaptcha
from checkbird import *
from detect_recaptcha import *
data = ""



#data = "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"
def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='checkbird.pt', help='checkbird.pt path(s)')
    parser.add_argument('--source', type=str, default='data/images', help='file/dir/URL/glob, 0 for webcam')
    parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=[640], help='inference size h,w')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='NMS IoU threshold')
    parser.add_argument('--max-det', type=int, default=1000, help='maximum detections per image')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='show results')
    parser.add_argument('--save-txt', default=False, action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--save-crop', default=False, action='store_true', help='save cropped prediction boxes')
    parser.add_argument('--nosave', default = True, action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3') #--class 0 1 2 3 4 5 6 7 8 9 10 11 12
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--visualize', action='store_true', help='visualize features')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--line-thickness', default=3, type=int, help='bounding box thickness (pixels)')
    parser.add_argument('--hide-labels', default=False, action='store_true', help='hide labels')
    parser.add_argument('--hide-conf', default=False, action='store_true', help='hide confidences')
    parser.add_argument('--half', action='store_true', help='use FP16 half-precision inference')
    opt = parser.parse_args()
    opt.imgsz *= 2 if len(opt.imgsz) == 1 else 1  # expand
    return opt
def parse_opt_rotate():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='rotate.pt', help='rotate.pt path(s)')
    parser.add_argument('--source', type=str, default='data/images', help='file/dir/URL/glob, 0 for webcam')
    parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=[640], help='inference size h,w')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='NMS IoU threshold')
    parser.add_argument('--max-det', type=int, default=1000, help='maximum detections per image')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='show results')
    parser.add_argument('--save-txt', default=False, action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--save-crop', default=False, action='store_true', help='save cropped prediction boxes')
    parser.add_argument('--nosave', default = True, action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3') #--class 0 1 2 3 4 5 6 7 8 9 10 11 12
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--visualize', action='store_true', help='visualize features')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--line-thickness', default=3, type=int, help='bounding box thickness (pixels)')
    parser.add_argument('--hide-labels', default=False, action='store_true', help='hide labels')
    parser.add_argument('--hide-conf', default=False, action='store_true', help='hide confidences')
    parser.add_argument('--half', action='store_true', help='use FP16 half-precision inference')
    opt = parser.parse_args()
    opt.imgsz *= 2 if len(opt.imgsz) == 1 else 1  # expand
    return opt

def parse_opt_funcaptcha():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='funcaptcha.pt', help='funcaptcha.pt path(s)')
    parser.add_argument('--source', type=str, default='data/images', help='file/dir/URL/glob, 0 for webcam')
    parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=[640], help='inference size h,w')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='NMS IoU threshold')
    parser.add_argument('--max-det', type=int, default=1000, help='maximum detections per image')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='show results')
    parser.add_argument('--save-txt', default=False, action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--save-crop', default=False, action='store_true', help='save cropped prediction boxes')
    parser.add_argument('--nosave', default = True, action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3') #--class 0 1 2 3 4 5 6 7 8 9 10 11 12
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--visualize', action='store_true', help='visualize features')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--line-thickness', default=3, type=int, help='bounding box thickness (pixels)')
    parser.add_argument('--hide-labels', default=False, action='store_true', help='hide labels')
    parser.add_argument('--hide-conf', default=False, action='store_true', help='hide confidences')
    parser.add_argument('--half', action='store_true', help='use FP16 half-precision inference')
    opt = parser.parse_args()
    opt.imgsz *= 2 if len(opt.imgsz) == 1 else 1  # expand
    return opt

api_key = "7z5w7qEedErY51yXLjQ"
url_gettask_captchatext = 'https://simplecaptcha.net/api/v1/ResolveCaptcha?key='+api_key+'&numWantGet=1&captchaType=all'
url_gettask_recaptcha = 'https://simplecaptcha.net/api/v1/ResolveCaptcha?key='+api_key+'&numWantGet=1&captchaType=recaptcha'
url_respon = 'https://simplecaptcha.net/api/v1/ResolveCaptcha?key='+api_key
num_thread = 10
round_run = 0
linux = True
sl = '//'


opt = parse_opt()
print("LoadModel Check bird")
stride_img,imgsz_img,pt_img,device_img,onnx_img,half_img,model_img,classify_img,names_img = checkbird.LoadModel(**vars(opt))
opt_rotate = parse_opt_rotate()
print("LoadModel Rotate")
stride_ro,imgsz_ro,pt_ro,device_ro,onnx_ro,half_ro,model_ro,classify_ro,names_ro = checkbird.LoadModel(**vars(opt_rotate))

opt_funcaptcha = parse_opt_funcaptcha()
print("LoadModel Funcaptcha")
stride_re,imgsz_re,pt_re,device_re,onnx_re,half_re,model_re,classify_re,names_re = checkbird.LoadModel(**vars(opt_funcaptcha))



#with open("image.jpg", "rb") as image_file:
    #data = base64.b64encode(image_file.read())


class myThread (threading.Thread):
   def __init__(self, threadID, name, counter, opt, opt_recaptcha ,images_folder="", result_folder=""):
        global sl
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.opt = opt
        self.opt_recaptcha = opt_recaptcha
        current_path = os.getcwd()
        current_path = current_path.replace("\\","//")
        if os.path.isdir(f"{current_path}{sl}data{sl}{self.name}") != True:
            os.mkdir(f"{current_path}{sl}data{sl}{self.name}")
        self.images_folder = f"{current_path}{sl}data{sl}{self.name}{sl}images"
        if os.path.isdir(self.images_folder) != True:
            os.mkdir(self.images_folder)
        self.result_folder = f"{current_path}{sl}data{sl}result"
        if os.path.isdir(self.result_folder) != True:
            os.mkdir(self.result_folder)
   def run(self):
        #Solver_Captcha(self, api_key, url_gettask, data)
        get_task_captchatext(self,api_key, url_gettask_captchatext, self.name, self.images_folder, self.result_folder)

class myThread2 (threading.Thread):
   def __init__(self, threadID, name, counter, opt, opt_recaptcha ,images_folder="", result_folder=""):
        global sl
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.opt = opt
        self.opt_recaptcha = opt_recaptcha
        current_path = os.getcwd()
        current_path = current_path.replace("\\","//")
        if os.path.isdir(f"{current_path}{sl}data{sl}{self.name}") != True:
            os.mkdir(f"{current_path}{sl}data{sl}{self.name}")
        self.images_folder = f"{current_path}{sl}data{sl}{self.name}{sl}images"
        if os.path.isdir(self.images_folder) != True:
            os.mkdir(self.images_folder)
        self.result_folder = f"{current_path}{sl}data{sl}result"
        if os.path.isdir(self.result_folder) != True:
            os.mkdir(self.result_folder)
   def run(self):
        #Solver_Captcha(self, api_key, url_gettask, data)
        get_task_recaptcha(self,api_key, url_gettask_recaptcha, self.name, self.images_folder, self.result_folder)


def get_task_captchatext(self,api_key, url, path, images_folder,result_folder):
    global round_run

    #source = images_folder
    while True:
        try:
            result = requests.get(url,timeout = 5)
        except:
            print(f"{self.name} Error Get Task {result.status_code}")
        try:
            if(len(result.text)):
                data = result.json()
                id = data[0]['id']
                captcha = ""
                type ="jpeg"
                if data[0]["base64Image"] is not None:
                    base64s = data[0]['base64Image']
                    if "," in base64s:
                        type = base64s.split(',')[0]
                        base64s = base64s.split(',')[1]
                    if "jpeg" in type == True:
                        type = "jpeg"
                    elif "jpg" in type == True:
                        type = "jpeg"
                    else:
                        type = "png"
                    missing_padding = len(base64s) % 4
                    if missing_padding:
                        base64s += b'='* (4 - missing_padding)
                    im = Image.open(BytesIO(base64.b64decode(base64s)))
                    #print(im.mode)
                    if os.path.isfile(f"{images_folder}{sl}{id}.{type}"):
                        os.remove(f"{images_folder}{sl}{id}.{type}")
                    im.save(f"{images_folder}{sl}{id}.{type}", type)
                    source = f"{images_folder}{sl}{id}.{type}"
                    if im.mode in ("RGBA", "P"):
                        print(f"{id} RGBA")
                        # try:
                        #     background = Image.new("RGB", im.size, (255, 255, 255))
                        #     background.paste(im, mask=im.split()[3]) # 3 is the alpha channel
                        #     if os.path.isfile(f"{images_folder}{sl}{id}.{type}"):
                        #         os.remove(f"{images_folder}{sl}{id}.{type}")
                        #     background.save(f"{images_folder}{sl}{id}.{type}", type, quality=80)
                        #     source = f"{images_folder}{sl}{id}.{type}"
                        #     im = Image.open(source)
                        # except:
                        #     if os.path.isfile(f"{images_folder}{sl}{id}.{type}"):
                        #         os.remove(f"{images_folder}{sl}{id}.{type}")
                        #     im.save(f"{images_folder}{sl}{id}.{type}", type)
                        #     source = f"{images_folder}{sl}{id}.{type}"
                        #     im = Image.open(source)
                    # else:
                    #     if os.path.isfile(f"{images_folder}{sl}{id}.{type}"):
                    #         os.remove(f"{images_folder}{sl}{id}.{type}")
                    #     im.save(f"{images_folder}{sl}{id}.{type}", type)
                    #     source = f"{images_folder}{sl}{id}.{type}"
                if data[0]["captchaType"] == "imagecaptcha":
                    result_path = f"{result_folder}{sl}{id}.txt"
                    question = data[0]["questionText"]
                    if(question == "bird"):
                        checkbird.run(source,stride_img,imgsz_img,pt_img,device_img,onnx_img,half_img,model_img,classify_img,names_img)
                    elif(question == "rotate"):
                        checkbird.run(source,stride_ro,imgsz_ro,pt_ro,device_ro,onnx_ro,half_ro,model_ro,classify_ro,names_ro)
                    for i in range(5):
                        if os.path.exists(result_path):
                            file = open(result_path,"r+") 
                            captcha = file.read()
                            file.close()
                            if(captcha ==""): 
                                print("No result")
                            else: 
                                break
                        time.sleep(random.randint(1,2))
                elif data[0]["captchaType"] == "simplequestion":
                    question = data[0]["questionText"]
                    print(question)
                    if "please enter your answer in numbers:" in question:
                        captcha = caculator(question.split("please enter your answer in numbers:")[-1])
                    elif "please enter an answer in digits:" in question:
                        captcha = caculator(question.split("please enter an answer in digits:")[-1])
                    elif "enter text only if you are not human" in question:
                        captcha = "."
                    elif "trả lời:" in question or "Answer:" in question:
                        captcha = question.split("please enter an answer in digits:")[-1].lstrip()
                    elif "spam check:" in question and ("minus" in question or "+" in question or "plus" in question):
                        captcha = caculator(question.split("spam check:")[-1])
                    else:
                        captcha = ""
                elif data[0]["captchaType"] == "recaptcha":
                    getpoint = True
                    w = im.size[0]
                    h = im.size[1]
                    question = data[0]["questionText"]
                    print(question)
                    detect_size =[]
                    if "|" in question:
                        tmp = question
                        question = tmp.split('|')[0]
                        detect_size.append(int(tmp.split('|')[1]))
                        detect_size.append(int(tmp.split('|')[2]))
                    if question == "boats or ships":
                        question = "boat"
                    if question[-1] == "s" and question != "bus":
                        question = question[:-1]
                    if question == "vehicle":
                        class_detect_list = ["car", "motorcycle", "bicycle", "bus", "train", "truck", "airplane","taxi", "tractor"]
                    else: 
                        class_detect_list = [question]
                    print(h/w)
                    if float(h/w) >1.4:
                        crop_w = w
                        crop_h = h*0.2
                        im_title = im.crop((0, 0, crop_w, crop_h))
                        im_title.save(f"{images_folder}{sl}{id}_title.{type}")
                        source = f"{images_folder}{sl}{id}_title.{type}"
                        image_captcha.run(source,stride_re,imgsz_re,pt_re,device_re,onnx_re,half_re,model_re,classify_re,names_re)
                        if os.path.exists(f"{result_folder}{sl}{id}_title.txt"):
                            file = open(f"{result_folder}{sl}{id}_title.txt","r+") 
                            question = file.read()
                            file.close()
                        if question == "":
                            image_captcha.run(source,stride_img,imgsz_img,pt_img,device_img,onnx_img,half_img,model_img,classify_img,names_img)
                            if os.path.exists(f"{result_folder}{sl}{id}_title.txt"):
                                file = open(f"{result_folder}{sl}{id}_title.txt","r+") 
                                question = file.read()
                                file.close()
                                os.remove(f"{result_folder}{sl}{id}_title.txt")  
                        if question == "":
                            print("Recaptcha no have questionText and can't detect question")
                        else:
                            im_content = im.crop((0, crop_h, w, h))
                            im_content.save(f"{images_folder}{sl}{id}_content.{type}")
                            source = f"{images_folder}{sl}{id}_content.{type}"
                            result_path = f"{result_folder}{sl}{id}_content.txt"
                    else:
                        result_path = f"{result_folder}{sl}{id}.txt"
                    if question != "":
                        print(f"Detect Recaptcha with question {question}")
                        captcha = detect_recaptcha.run(source, stride_re,imgsz_re,pt_re,device_re,onnx_re,half_re,model_re,classify_re,names_re, class_detect_list, detect_size, getpoint)
                        # for i in range(5):
                        #     if os.path.exists(result_path):
                        #         file = open(result_path,"r+") 
                        #         captcha = file.read()
                        #         file.close()
                        #         break
                        #     else:
                        #         time.sleep(random.randint(1,2))
                        if captcha == "|":
                            captcha = "None"
                   
                   
                print(f"JobID:{id}, Result: {captcha}")
                #jsons = {'JobId':id,'Result':captcha, 'AnswerQuestion': captcha}
                #print(jsons)
                requests.post(url_respon, json = {'JobId':id,'Result':captcha, 'AnswerQuestion': captcha})
                #requests.post(url_respon, json = {'JobId':id,'Result':captcha})
                if os.path.isfile(result_path):
                    os.remove(result_path)  
                if os.path.exists(source):
                    os.remove(source) 
            else:
                time.sleep(random.randint(1,2))
                print(f"{self.name} no task")
        except:
            print(f"{self.name} Error Solover")
        #time.sleep(random.randint(2,5))
        round_run += 1

def get_task_recaptcha(self,api_key, url, path, images_folder,result_folder):
    global round_run
   
    
    #source = images_folder
    while True:
        try:
            result = requests.get(url,timeout = 5)
        except:
            print(f"{self.name} Error Get Task {result.status_code}")
        try:
            if(len(result.text)):
                data = result.json()
                id = data[0]['id']
                captcha = ""
                type ="jpeg"
                if data[0]["base64Image"] is not None:
                    base64s = data[0]['base64Image']
                    if "," in base64s:
                        type = base64s.split(',')[0]
                        base64s = base64s.split(',')[1]
                    if "jpeg" in type == True:
                        type = "jpeg"
                    elif "jpg" in type == True:
                        type = "jpeg"
                    else:
                        type = "png"
                    missing_padding = len(base64s) % 4
                    if missing_padding:
                        base64s += b'='* (4 - missing_padding)
                    im = Image.open(BytesIO(base64.b64decode(base64s)))
                    #print(im.mode)
                    if os.path.isfile(f"{images_folder}{sl}{id}.{type}"):
                        os.remove(f"{images_folder}{sl}{id}.{type}")
                    im.save(f"{images_folder}{sl}{id}.{type}", type)
                    source = f"{images_folder}{sl}{id}.{type}"
                    if im.mode in ("RGBA", "P"):
                        print(f"{id} RGBA")
                        # try:
                        #     background = Image.new("RGB", im.size, (255, 255, 255))
                        #     background.paste(im, mask=im.split()[3]) # 3 is the alpha channel
                        #     if os.path.isfile(f"{images_folder}{sl}{id}.{type}"):
                        #         os.remove(f"{images_folder}{sl}{id}.{type}")
                        #     background.save(f"{images_folder}{sl}{id}.{type}", type, quality=80)
                        #     source = f"{images_folder}{sl}{id}.{type}"
                        #     im = Image.open(source)
                        # except:
                        #     if os.path.isfile(f"{images_folder}{sl}{id}.{type}"):
                        #         os.remove(f"{images_folder}{sl}{id}.{type}")
                        #     im.save(f"{images_folder}{sl}{id}.{type}", type)
                        #     source = f"{images_folder}{sl}{id}.{type}"
                        #     im = Image.open(source)
                    # else:
                    #     if os.path.isfile(f"{images_folder}{sl}{id}.{type}"):
                    #         os.remove(f"{images_folder}{sl}{id}.{type}")
                    #     im.save(f"{images_folder}{sl}{id}.{type}", type)
                    #     source = f"{images_folder}{sl}{id}.{type}"
                if data[0]["captchaType"] == "imagecaptcha":
                    result_path = f"{result_folder}{sl}{id}.txt"
                    image_captcha.run(source,stride_img,imgsz_img,pt_img,device_img,onnx_img,half_img,model_img,classify_img,names_img)
                    for i in range(5):
                        if os.path.exists(result_path):
                            file = open(result_path,"r+") 
                            captcha = file.read()
                            file.close()
                            if captcha == "":
                                print(base64s)
                                #print("Convert RGB")
                                background = Image.new("RGB", im.size, (255, 255, 255))
                                background.paste(im, mask=im.split()[3]) # 3 is the alpha channel
                                if os.path.isfile(f"{images_folder}{sl}{id}.jpeg"):
                                    os.remove(f"{images_folder}{sl}{id}.jpeg")
                                background.save(f"{images_folder}{sl}{id}.jpeg", 'JPEG', quality=80)
                                source = f"{images_folder}{sl}{id}.jpeg"                  
                                image_captcha.run(source,stride_img,imgsz_img,pt_img,device_img,onnx_img,half_img,model_img,classify_img,names_img)
                                time.sleep(random.randint(1,2))
                                file = open(result_path,"r+") 
                                captcha = file.read()
                                file.close()
                                print(f"Convert RGB have result {captcha}")
                            break
                        time.sleep(random.randint(1,2))
                elif data[0]["captchaType"] == "simplequestion":
                    question = data[0]["questionText"]
                    print(question)
                    if "please enter your answer in numbers:" in question:
                        captcha = caculator(question.split("please enter your answer in numbers:")[-1])
                    elif "please enter an answer in digits:" in question:
                        captcha = caculator(question.split("please enter an answer in digits:")[-1])
                    elif "enter text only if you are not human" in question:
                        captcha = "."
                    elif "trả lời:" in question or "Answer:" in question:
                        captcha = question.split("please enter an answer in digits:")[-1].lstrip()
                    elif "spam check:" in question and ("minus" in question or "+" in question or "plus" in question):
                        captcha = caculator(question.split("spam check:")[-1])
                    else:
                        captcha = ""
                elif data[0]["captchaType"] == "recaptcha":
                    getpoint = False
                    w = im.size[0]
                    h = im.size[1]
                    question = data[0]["questionText"]
                    
                    detect_size =[]
                    if "|" in question:
                        tmp = question
                        question = tmp.split('|')[0]
                        detect_size.append(int(tmp.split('|')[1]))
                        detect_size.append(int(tmp.split('|')[2]))
                    if (question == "getpoint") or ("correct way up" in question) :
                        getpoint = True
                    if question == "boats or ships":
                        question = "boat"
                    if question[-1] == "s" and question != "bus":
                        question = question[:-1]
                    if question == "vehicle":
                        class_detect_list = ["car", "motorcycle", "bicycle", "bus", "train", "truck", "airplane","taxi", "tractor"]
                    else: 
                        class_detect_list = [question]
                    print(h/w)
                    if float(h/w) >1.4:
                        crop_w = w
                        crop_h = h*0.2
                        im_title = im.crop((0, 0, crop_w, crop_h))
                        im_title.save(f"{images_folder}{sl}{id}_title.{type}")
                        source = f"{images_folder}{sl}{id}_title.{type}"
                        image_captcha.run(source,stride_re,imgsz_re,pt_re,device_re,onnx_re,half_re,model_re,classify_re,names_re)
                        if os.path.exists(f"{result_folder}{sl}{id}_title.txt"):
                            file = open(f"{result_folder}{sl}{id}_title.txt","r+") 
                            question = file.read()
                            file.close()
                        if question == "":
                            image_captcha.run(source,stride_img,imgsz_img,pt_img,device_img,onnx_img,half_img,model_img,classify_img,names_img)
                            if os.path.exists(f"{result_folder}{sl}{id}_title.txt"):
                                file = open(f"{result_folder}{sl}{id}_title.txt","r+") 
                                question = file.read()
                                file.close()
                                os.remove(f"{result_folder}{sl}{id}_title.txt")  
                        if question == "":
                            print("Recaptcha no have questionText and can't detect question")
                        else:
                            im_content = im.crop((0, crop_h, w, h))
                            im_content.save(f"{images_folder}{sl}{id}_content.{type}")
                            source = f"{images_folder}{sl}{id}_content.{type}"
                            result_path = f"{result_folder}{sl}{id}_content.txt"
                    else:
                        result_path = f"{result_folder}{sl}{id}.txt"
                    if question != "":
                        print(f"Detect Recaptcha with question {question}")
                        captcha = detect_recaptcha.run(source, stride_re,imgsz_re,pt_re,device_re,onnx_re,half_re,model_re,classify_re,names_re, class_detect_list, detect_size, getpoint)
                        # for i in range(5):
                        #     if os.path.exists(result_path):
                        #         file = open(result_path,"r+") 
                        #         captcha = file.read()
                        #         file.close()
                        #         break
                        #     else:
                        #         time.sleep(random.randint(1,2))
                        if captcha == "|":
                            captcha = "None"
                   
                print(f"JobID:{id}, Result: {captcha}")
                #jsons = {'JobId':id,'Result':captcha, 'AnswerQuestion': captcha}
                #print(jsons)
                requests.post(url_respon, json = {'JobId':id,'Result':captcha, 'AnswerQuestion': captcha})
                #requests.post(url_respon, json = {'JobId':id,'Result':captcha})
                if os.path.isfile(result_path):
                    os.remove(result_path)  
                if os.path.exists(source):
                    os.remove(source) 
            else:
                time.sleep(random.randint(1,2))
                print(f"{self.name} no task")
        except:
            print(f"{self.name} Error Solover")
        #time.sleep(random.randint(2,5))
        round_run += 1
        
def Solver_Captcha(self,api_key, url, base64s):
    type ="png"
    id = 9999
    images_folder = self.images_folder
    result_folder = self.result_folder
    stride,imgsz,pt,device,onnx,half,model,classify,names = image_captcha.LoadModel(**vars(self.opt_recaptcha))
    im = Image.open(BytesIO(base64.b64decode(base64s)))
    w = im.size[0]
    h = im.size[1]
    getpoint = False
    question = "getpoint"
    detect_size =[]
    if "|" in question:
        tmp = question
        question = tmp.split('|')[0]
        detect_size.append(int(tmp.split('|')[1]))
        detect_size.append(int(tmp.split('|')[2]))
    if question == "getpoint":
        getpoint = True
    if question == "boats or ships":
        question = "boat"
    if question[-1] == "s" and question != "bus":
        question = question[:-1]
    if question == "vehicle":
        class_detect_list = ["car", "motorcycle", "bicycle", "bus", "train", "truck", "airplane","taxi", "tractor"]
    else: 
        class_detect_list = [question]
    print(h/w)
    if float(h/w) >1.4:
        crop_w = w
        crop_h = h*0.2
        im_title = im.crop((0, 0, crop_w, crop_h))
        im_title.save(f"{images_folder}{sl}{id}_title.{type}")
        source = f"{images_folder}{sl}{id}_title.{type}"
        image_captcha.run(source,stride,imgsz,pt,device,onnx,half,model,classify,names)
        if os.path.exists(f"{result_folder}{sl}{id}_title.txt"):
            file = open(f"{result_folder}{sl}{id}_title.txt","r+") 
            question = file.read()
            file.close()
        # if question == "":
            # image_captcha.run(source,stride_img,imgsz_img,pt_img,device_img,onnx_img,half_img,model_img,classify_img,names_img)
            # if os.path.exists(f"{result_folder}{sl}{id}_title.txt"):
            #     file = open(f"{result_folder}{sl}{id}_title.txt","r+") 
            #     question = file.read()
            #     file.close()
            #     os.remove(f"{result_folder}{sl}{id}_title.txt")  
        if question == "":
            print("Recaptcha no have questionText and can't detect question")
        else:
            im_content = im.crop((0, crop_h, w, h))
            im_content.save(f"{images_folder}{sl}{id}_content.{type}")
            source = f"{images_folder}{sl}{id}_content.{type}"
            result_path = f"{result_folder}{sl}{id}_content.txt"
    else:
        result_path = f"{result_folder}{sl}{id}.txt"
    if question != "":
        print(f"Detect Recaptcha with question {question}")
        detect_recaptcha.run(source, stride,imgsz,pt,device,onnx,half,model,classify,names, class_detect_list, detect_size,getpoint)
        if os.path.exists(result_path):
            file = open(result_path,"r+") 
        captcha = file.read()
        file.close()
        if captcha == "|":
            captcha = "None"
                   
def CheckQuestion(self, question):
    if "please enter your answer in numbers:" in question:
        captcha = caculator(question.split("please enter your answer in numbers:")[-1])
    elif "please enter an answer in digits:" in question:
        captcha = caculator(question.split("please enter an answer in digits:")[-1])
    elif "enter text only if you are not human" in question:
        captcha = "."
    elif "trả lời:" in question or "Answer:" in question:
        captcha = question.split("please enter an answer in digits:")[-1].lstrip()
    elif "spam check:" in question and ("minus" in question or "+" in question or "plus" in question):
        captcha = caculator(question.split("spam check:")[-1])
    else:
        captcha = "."   


# Create new threads
if __name__ == "__main__":
    
    # with open(f"test.png", "rb") as image_file:
    #     encode64 = base64.b64encode(image_file.read()).decode("utf-8")
    #     image_file.close()
    # data = encode64
    for i in range(num_thread):
        thread = myThread(i+1, f"Thread-text-{i+1}", i+1, opt, opt_recaptcha)
        thread.start()
        time.sleep(random.randint(15,30))
        #thread2 = myThread2(i+1, f"Thread-recaptcha-{i+1}", i+1, opt, opt_recaptcha)
        #thread2.start()
        #time.sleep(random.randint(15,30))
    while(True):
        if round_run >=50:
            round_run =0
            if linux ==False:
                clear = lambda: os.system('cls')
                clear()
            else:
                clear_output()


 


