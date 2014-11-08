#import facebook
from facepy import GraphAPI
from facepy import utils 

def main():
    app_id = 1486791588264932
    app_secret = "93595d85e282ce2bb395a21c92139631"
    oath_access_token = utils.get_application_access_token(app_id, app_secret)
    
    token = "CAACEdEose0cBAHdKj7pO0wWcQ1l7Nk5SXOUZAWdIEOZCvFg6JuL8IRJQcTJZBg
    GpNgoO5M2d3nZBYOhOdnDgn9gJc9mZCk8bC9N5yIMAEVpZAWX8pgIv
    CSZCGWu6vkfX5I1VDCfkyLHaKkxpgLOyTsnOCHuWkiBrjlW5dN1IHNLmZ
    C168XZBMJIc1r5UA7ssNZAUhJPsbNzaR1rer93oSuQA4kZAfNIjGCp95IZD"
    
    print oath_access_token
    
    graph = GraphAPI(token)
    
    for friendlist in graph.get('me/friendlists/')["data"]:
        print
        
        for friend in graph.get( friendlist["id"] + "/members" )["data"]:
            print friend["name"]

            try:    
            print len( graph.get(friend["id"] + "/friends/")["data"] )
                print len(frnd_friendlist)
            except :
                print 0
            
   
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)