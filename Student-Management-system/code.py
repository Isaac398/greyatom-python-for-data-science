# --------------
class_1=['Geoffery Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class= class_1 + class_2
print(new_class)
print('='*30)
new_class.append('Peter Warden')
print(new_class)
print('='*30)
new_class.remove('Carla Gentry')
print(new_class)
print('='*30)
cources={'Math':60,'English':70,'History':80,'French':70,'Science':60}
total=(60+70+80+70+60)
print('total is:','{0:.2f}'.format(total))
percentage=(total/500)*100
print('percentage is=','{0:.2f}'.format(percentage))
cources={'Math':65,'English':70,'History':80,'French':70,'Science':60}
total=(65+70+80+70+60)
print('updated total is:','{0:.2f}'.format(total))
percentage=(total/500)*100
print('updated percentage is=','{0:.2f}'.format(percentage))
mathematics={"Geoffery Hinton":78,"Andrew Ng":95,"Sebastian Raschka":65,"Yoshua Bengio":50,
              "Hilary Mason":70,"Corinna Cortes":66,"Peter Warden":	75}
max_marks_scored=max(mathematics,key = mathematics.get)
print(max_marks_scored) 
topper = 'Andrew Ng'  
print("topper is:",topper) 
topper.split()  
first_name='Andrew'
last_name='Ng'
full_name= last_name+" "+first_name
print(full_name)
certificate_name=full_name.upper()
print('certificate_name is',certificate_name)





