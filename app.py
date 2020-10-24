from flask import Flask, render_template, url_for

app = Flask(__name__)
 

@app.route('/')
def main():
    return render_template('main.html')

#@app.route('/<post_name>') #動的ルーティング
#def show_post(post_name):
#    print(type(post_name))
#    return 'Post {}'.format(post_name)

if __name__=='__main__':
    app.run()