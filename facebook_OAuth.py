 # Credentials of APP

import ssl
client_id = '1184399584913921'
client_secret = 'e5634ae345fdda136e251cae7e31091e'

# OAuth endpoints given in the Facebook API documentation
authorization_base_url = 'https://www.facebook.com/dialog/oauth'
token_url = 'https://graph.facebook.com/oauth/access_token'
redirect_uri = 'https://tdas4-ece9065-lab3-cloned-tdas4.c9users.io/'     

from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix
facebook = OAuth2Session(client_id, redirect_uri=redirect_uri)
facebook = facebook_compliance_fix(facebook)

# Redirect user to Facebook for authorization
authorization_url, state = facebook.authorization_url(authorization_base_url)
print 'Please go here and authorize,', authorization_url

# Get the authorization verifier code from the callback url
redirect_response = raw_input('Paste the full redirect URL here:')

# Fetch the access token
facebook.fetch_token(token_url, client_secret=client_secret,authorization_response=redirect_response)

# Fetch a protected resource, i.e. user profile
r = facebook.get('https://graph.facebook.com/me?')
print r.content