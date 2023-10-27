#dictionary
#implicit
#syntax:variableName={key:value,key,value}
userDetails = {'fistName': 'Thulasi', 'lastName': 'latha', 'Email': 'thulasilatha501@gmail.com'}
print(type(userDetails))

#explicit
#syntax:variableName=dict{key:value,key:value}

userDetails = dict({'firstName': 'Thulasi', 'lastName': 'latha', 'Email': 'thulasilatha501@gmail.com'})
print(type(userDetails))

#datatype/variable Annotation
#syntax:variableName:dict={key:value,key:value}
userDetails:dict = {'fistName': 'Thulasi', 'lastName': 'latha', 'Email':'thulasilatha501@gmsil.com'}
print(type(userDetails))