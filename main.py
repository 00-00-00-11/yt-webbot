from webbot import Browser

web = Browser() #this opens the browser
web.go_to('google.com') # this is ur site which u want bot to open.u can edit it too !
web.type('hello its me')  #it is not imp to do but if u want it to say then u can,

web.press(web.Key.ENTER)#it is example which can make it press enter or any other key
web.go_back() #if u want bot to go back to the site if the link was opened any where else
web.click('Sign in') #this is too imp it clicks the button but text scan
web.type('xyzyzyz@gmail.com' , into='Email') #this types in the sign in email
web.click('NEXT' , tag='span')
web.type('mxyzyzyz' , into='Password' , id='passwordFieldId')
web.click('NEXT' , tag='span') # you are logged in
