from flask import Flask, render_template, flash, redirect,url_for
from urllib.request import urlopen
from query import Query, Category
from urllib.parse import urlencode, quote
import json

file = open('C:\\solr-7.7.3\\example\\exampledocs\\movie.json','rb')
dic = json.load(file)
file.close()

app =  Flask(__name__)
app.config['SECRET_KEY'] ='d15cbf7bf6e6b9d6ee13b2168d6a9e036c41de81dcd58987ff04df7898a86f24'
@app.route('/docs')
def doc_info():
    return render_template('docs.html')

@app.route('/', methods=['POST','GET'])
@app.route('/home', methods=['POST','GET'])
def hello_world():
    qury = Query()
    #checkbox = Category()
    #print(qury.checkbox.data)
    try:
        query =  "\""+qury.search.data+"\""
        query =  quote("authors:"+query)
        #print('http://localhost:8983/solr/try_books1/select?q={}&wt=python'.format(query))
        print('query submit',qury.validate_on_submit())
        if qury.validate_on_submit():
            if(qury.checkbox_title.data):
                query =  "\""+qury.search.data+"\""  
                query =  quote("Title:"+query)
                url='http://localhost:8983/solr/movies_2/select?q={}&rows=20&wt=python'.format(query)
                #print('url',url)
            if(qury.select_genre.data):
                if(qury.checkbox_title.data):
                    query =  "\""+qury.search.data+"\""  
                    query =  quote("Title:"+query)
                    query2 =  qury.select_genre.data
                    query2 =  quote("Genre:"+query2)
                    if(qury.select_genre.data=='None'):
                        final = query
                    else:
                        final = query + quote(" AND ") + query2
                    url='http://localhost:8983/solr/movies_2/select?q={}&rows=20&wt=python'.format(final)
                else:
                 query =  qury.select_genre.data
                 query =  quote("Genre:"+query)
                 url='http://localhost:8983/solr/movies_2/select?q={}&rows=20&wt=python'.format(query)
            if(qury.checkbox_plot.data):
                query =  qury.search.data
                query =  quote("Plot:"+query)
                url='http://localhost:8983/solr/movies_2/select?q={}&rows=20&wt=python'.format(query)
            print('url:',url)
            
            conn = urlopen(url)
            content = eval( conn.read())['response']
            print('content',content)
            #print(content)
            flash(f'query searched {qury.search.data}!')
            return render_template('docs.html',content=content)
            #return content
   
    except:
        pass
    return render_template('home.html',form = qury)
    #return content

@app.route('/about')
def about():
    qury = Query()
    return render_template('about.html',form = qury)

if __name__ == '__main__':
    
    app.run(debug =True)
