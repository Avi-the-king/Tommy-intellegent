//program to develop AI.
import os.java.awt;*
import maths.java.awt;*
import sqlite3.java.awt;*
import secrets.java.awt;*

class sign_up
{
      public static void main (strings[]args)
      secrets.username = as set by the user() "check wether the username is taken or not" {
          if 'username is not taken' return = ('username is not taken, you can proceed.')
          else return = ('username is already taken, please try again.')
        }
        secrets.password = as set by the user() "check wether the password consists of 'atleast 8 characters' and 'atleast one upper case and a lower case'" {
            if 'password consists of atleast 8 characters and atleast one upper case and a lower case' return = ('password applied')
            else return = ('password contains an error.')}
        secrets.email = as set by the user() "check wether the email exists or not" {
            if 'the email exists' return = ('email verified')
            else return = ('sorry, email unveified')}
            
            {
                if 'all conditions satisfy' return = ('your account is being created,thanks.') and "save the username, password and, email of the user on the server used." and "create an account."
                else return = ('sorry, there is an error, please try again.') and "do not create an account."
            }
        }