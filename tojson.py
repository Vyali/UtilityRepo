import json
import sys

def write_tab(f,n):
    tab= '\t'
    for i in range(n):
        f.write(tab)

def write_new_line(f,n):
    new_line = '\n'
    for i in range(n):
        f.write(new_line)

def gen_class(cname,f):
    print('generating class '+cname)
    str = 'public class '+cname+'{'
    f.write(str)
    write_new_line(f,2)
    

def gen_variables(name,attrib,f):
    print('generating variable'+name)
    attrib.setdefault('modifier','private')    
    
    str = attrib['modifier'] + ' ' + attrib['type'] + ' '+name+';'
    write_tab(f,1)
    f.write(str)
    write_new_line(f,1)
 
    
def gen_setter(name,return_type,f):
    method_name = 'set'+name[0].upper()+name[1:]
    str = 'public void '+method_name +'( '+return_type +' '+ name +' ){'
    f.write(str)
    write_new_line(f,1)
    write_tab(f,2)
    logic = 'this.'+name+' = '+ name +';'
    f.write(logic)
    write_new_line(f,1)
    write_tab(f,1)
    f.write('}')
    write_new_line(f,1)
    
def gen_getter(name,return_type,f):
    method_name = 'get'+name[0].upper()+name[1:]
    str = 'public '+return_type +' '+method_name
    str = str+'(){'
    
    f.write(str)
    write_new_line(f,1)
    write_tab(f,2)
    str = 'return '+ name +';'
    f.write(str)
    write_new_line(f,1)
    write_tab(f,1)
    f.write('}')
    write_new_line(f,1)
    

def gen_methods(name,attrib,f):
    print('generating method')
    return_type = attrib['type']
    
    print(return_type)
    write_tab(f,1)
    gen_getter(name,return_type,f)
    write_tab(f,1)
    gen_setter(name,return_type,f)
    
   
       

    
    
json_data = {}
cl={}

with open('pojojson.json', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)
    
print(json_data)

    

cl = json_data.get('class')
cln = cl['name']
f = open(cln+'.java','w')
try:
    gen_class(cln,f)
    cla = cl['attributes'] 
    for a in cla:
        gen_variables(a,cla[a],f)
     
    write_new_line(f,2)    
    for a in cla:
        gen_methods(a,cla[a],f)    
        
 

   
    
    
except:
    print("wrong")
    print("Oops!",sys.exc_info()[0],"occured.")
finally:
    f.close()    
    
''''
f2 = open(cln+'.java','w')
try:
    
    cla = cl['attributes'] 
    for a in cla:
        gen_methods(a,cla[a],f2)
    
except:
    print("Oops f2!",sys.exc_info()[0],"occured.")
finally:
    f2.close
    
        

'''



    
    