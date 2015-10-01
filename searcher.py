#!/usr/bin/python
import cgi
import cgitb
from os import listdir					
from os.path import isfile,join			
from whoosh.index import create_in		
from whoosh.fields import *				
from BeautifulSoup import BeautifulSoup	
from whoosh.writing import AsyncWriter	
import time
import sys
from whoosh.qparser import QueryParser
import whoosh.index as index
from whoosh import scoring
from time import ctime

len_bm25=0
len_tf=0
len_tf_idf=0
BM25 = None
tf=None
tf_idf=None
BM25_counter = None
tf_counter=None
tf_idf_counter=None
page_number=1
page_counter_bm_25=0
page_counter_idf=0
page_counter_tf=0
flag_bm25=None
flag_tf_idf=None
flag_tf=None
page_number_idf=1
page_number_tf=1
form = cgi.FieldStorage()
my_query=form.getvalue('query')
my_selection = form.getvalue('selection')
flag_bm25= form.getvalue('flag_bm25')
flag_tf_idf=form.getvalue('flag_tf_idf')
flag_tf=form.getvalue('flag_tf')
if flag_bm25==None:
	flag_bm25="1"
if flag_tf==None:
	flag_tf="1"
if flag_tf_idf==None:
	flag_tf_idf="1"
if form.getvalue('my_page_number')!=None:
	page_number= int(form.getvalue('my_page_number'))
if form.getvalue('my_page_number_idf')!=None:
	page_number_idf= int(form.getvalue('my_page_number_idf'))
if form.getvalue('my_page_number_tf')!=None:
	page_number_tf= int(form.getvalue('my_page_number_tf'))
if my_selection!=None:
	if my_selection=="Simple":
		ix_bm25 = index.open_dir("index")
		searcher= ix_bm25.searcher()
		if my_query!=None:
			new_query = QueryParser("content", ix_bm25.schema).parse(unicode(my_query))
			BM25_counter = searcher.search(new_query)
			BM25 = searcher.search_page(new_query,int(page_number),10)


		ix_tf_idf = index.open_dir("index")	
		searcher_idf= ix_tf_idf.searcher(weighting=scoring.TF_IDF())
		if my_query!=None:
			new_query_idf = QueryParser("content",ix_tf_idf.schema).parse(unicode(my_query))
			tf_idf_counter = searcher_idf.search(new_query_idf)
			tf_idf= searcher_idf.search_page(new_query_idf,int(page_number_idf),10)

		ix_tf= index.open_dir("index")
		searcher_tf= ix_tf.searcher(weighting=scoring.Frequency())
		if my_query!=None:
			new_query_tf= QueryParser("content",ix_tf.schema).parse(unicode(my_query))
			tf_counter = searcher_tf.search(new_query_tf)
			tf=searcher_tf.search_page(new_query_tf,int(page_number_tf),10)

if my_selection!=None:
	if my_selection=="Stemming and Stop":
		ix_bm25 = index.open_dir("stemming_and_stop")
		searcher= ix_bm25.searcher()
		if my_query!=None:
			new_query = QueryParser("content", ix_bm25.schema).parse(unicode(my_query))
			BM25_counter = searcher.search(new_query)
			BM25 = searcher.search_page(new_query,int(page_number),10)

		ix_tf_idf = index.open_dir("stemming_and_stop")	
		searcher_idf= ix_tf_idf.searcher(weighting=scoring.TF_IDF())
		if my_query!=None:
			new_query_idf = QueryParser("content",ix_tf_idf.schema).parse(unicode(my_query))
			tf_idf_counter = searcher_idf.search(new_query_idf)
			tf_idf= searcher_idf.search_page(new_query_idf,int(page_number_idf),10)

		ix_tf= index.open_dir("stemming_and_stop")
		searcher_tf= ix_tf.searcher(weighting=scoring.Frequency())
		if my_query!=None:
			new_query_tf= QueryParser("content",ix_tf.schema).parse(unicode(my_query))
			tf_counter = searcher_tf.search(new_query_tf)
			tf=searcher_tf.search_page(new_query_tf,int(page_number_tf),10)
if my_selection!=None:
	if my_selection=="Stemming without Stop":
		ix_bm25 = index.open_dir("stemming_without_stop")
		searcher= ix_bm25.searcher()
		if my_query!=None:
			new_query = QueryParser("content", ix_bm25.schema).parse(unicode(my_query))
			BM25_counter = searcher.search(new_query)
			BM25 = searcher.search_page(new_query,int(page_number),10)

		ix_tf_idf = index.open_dir("stemming_without_stop")	
		searcher_idf= ix_tf_idf.searcher(weighting=scoring.TF_IDF())
		if my_query!=None:
			new_query_idf = QueryParser("content",ix_tf_idf.schema).parse(unicode(my_query))
			tf_idf_counter = searcher_idf.search(new_query_idf)
			tf_idf= searcher_idf.search_page(new_query_idf,int(page_number_idf),10)

		ix_tf= index.open_dir("stemming_without_stop")
		searcher_tf= ix_tf.searcher(weighting=scoring.Frequency())
		if my_query!=None:
			new_query_tf= QueryParser("content",ix_tf.schema).parse(unicode(my_query))
			tf_counter = searcher_tf.search(new_query_tf)
			tf=searcher_tf.search_page(new_query_tf,int(page_number_tf),10)
if my_selection!=None:
	if my_selection=="Stop without Stemming":
		ix_bm25 = index.open_dir("stop_without_stemming")
		searcher= ix_bm25.searcher()
		if my_query!=None:
			new_query = QueryParser("content", ix_bm25.schema).parse(unicode(my_query))
			BM25_counter = searcher.search(new_query)
			BM25 = searcher.search_page(new_query,int(page_number),10)

		ix_tf_idf = index.open_dir("stop_without_stemming")	
		searcher_idf= ix_tf_idf.searcher(weighting=scoring.TF_IDF())
		if my_query!=None:
			new_query_idf = QueryParser("content",ix_tf_idf.schema).parse(unicode(my_query))
			tf_idf_counter = searcher_idf.search(new_query_idf)
			tf_idf= searcher_idf.search_page(new_query_idf,int(page_number_idf),10)

		ix_tf= index.open_dir("stop_without_stemming")
		searcher_tf= ix_tf.searcher(weighting=scoring.Frequency())
		if my_query!=None:
			new_query_tf= QueryParser("content",ix_tf.schema).parse(unicode(my_query))
			tf_counter = searcher_tf.search(new_query_tf)
			tf=searcher_tf.search_page(new_query_tf,int(page_number_tf),10)		
#ef main_page():
print "Content-type:text/html"
print
print ('''
	<!DOCTYPE html>
<html>
	<head>
		<title>
			Information Retrieval
		</title>
		
		<link href="Bootstrap/css/bootstrap.css" rel="stylesheet">
		<link href="Bootstrap/css/bootstrap.min.css" rel="stylesheet">
		<link href="Bootstrap/css/bootstrap-theme.css" rel="stylesheet">
		<link href="Bootstrap/css/bootstrap-theme.min.css" rel="stylesheet">
		<script src="Bootstrap/js/jquery-2.1.3.min.js"></script>
        <script src="Bootstrap/js/bootstrap.min.js"></script>
        <script type="text/javascript" src="lib/jquery.bootpag.js"></script>
        
	</head>
	
	<body>
		<div align="center" class="page-header" style="margin-top: 10px;">
			 	<h2 style="color:blue" >INFO FINDER</h2>
		</div>
		
			<form action="#" method="post" id="my_form">
			  	<div class="col-lg-6" style=" margin-left:260px;">
			  		<input type="hidden" name="my_page_number" id="my_page_number">
			  		<input type="hidden" name="my_page_number_idf" id="my_page_number_idf">
			  		<input type="hidden" name="my_page_number_tf" id="my_page_number_tf">
			  		<input type="hidden" name="flag_bm25" id="flag_bm25">
			  		<input type="hidden" name="flag_tf" id="flag_tf">
			  		<input type="hidden" name="flag_tf_idf" id="flag_tf_idf">
					<div class="input-group">
	  					<input type="text" id="query" name="query" class="form-control" placeholder="Search for...">
	  						<span class="input-group-btn">
	   					 		<button type="submit" value="Submit" class="btn btn-default">Go!
	   					 		</button>
	  						</span>
					</div><!-- /input-group -->
	 			</div><!-- /.col-lg-6 -->
	 			
				<div class="btn-group" style=" margin-left:230px;">
						<button type="button" class="btn btn-success">Analysis</button>
							<button type="button" class="btn btn-success dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
						<span class="caret"></span>
						<span class="sr-only">Toggle Dropdown</span>
						</button>
	  				<ul class="dropdown-menu">
					   	<li><a href="analysis.jpg">Analysis</a></li>
					    <li><a href="map.py">MAP</a></li>
					    <li><a href="ndcg.py">NDCG</a></li>
					    <li role="separator" class="divider"></li>
					    
	 				 </ul>
				</div>
				<select name="selection" id="selection" class="form-control" style="max-width:14%; margin-top: -33px;">
				    <option value="Stemming and Stop">Stemming and Stop</option>
				    <option value="Stemming without Stop">Stemming without Stop</option>
				    <option value="Stop without Stemming">Stop without Stemming</option>
				    <option value="Simple">Simple</option>
				    
				</select>
				
			</form>
		
	<div class="container-fluid" style="margin-top: 20px;">
		<div class="row">
			<div class="col-lg-4 col-md-4">
				<div class="panel panel-primary">
        			<div class="panel-heading">BM25</div>


              			<div class="panel-body" style="min-height: 500px; max-height: 500px;overflow-y: scroll;">''')

if BM25!=None:
	x = 0
	for result in BM25:
		x = x + 1
		link_string = "<a class='result_link' "
		link_string = link_string + " data-query="
		link_string = link_string + my_query
		link_string = link_string + " data-time="
		link_string = link_string + ctime()
		link_string = link_string + " data-path="
		link_string = link_string + str(result['path'].encode("utf-8"))
		link_string = link_string + " data-technique="
		link_string = link_string + "BM25"
		link_string = link_string + " data-page="
		link_string = link_string + str(page_number)
		link_string = link_string + " data-number="
		link_string = link_string + str(x)
		link_string = link_string + " data-title="
		link_string = link_string + str(result['title'].encode("utf-8"))
		link_string = link_string + " href="
		link_string = link_string + result['path'].encode("utf-8")
		link_string = link_string + ">"
		link_name 	= result['title'].encode("utf-8")
		link_string = link_string + link_name+"</a><br>\n"
		print link_string
		print result['path'].encode("utf-8")

		print "<br/>"
		print "<br/>"
		print result.highlights("content").encode("utf-8")
		#print(result.highlights("content"))
		print "<br/>"
		print "<br/>"
if tf_idf!=None:
	if len(tf_idf)%10 == 0:
		len_tf_idf= len(tf_idf)/10
	else:
		len_tf_idf= len(tf_idf)/10 +1
if BM25!=None:
	if len(BM25)%10 == 0:
		len_bm25= len(BM25)/10
	else:
		len_bm25= len(BM25)/10 +1
if tf!=None:
	if len(tf)%10 == 0:
		len_tf= len(tf)/10
	else:
		len_tf= len(tf)/10 +1
print('''</div>
        		</div>
        			<div class="bs-docs-example">
                        <p style="margin-left:90px" class="demo demo2"></p>
                    </div>
                 	
				</div>
		  		
		  	<div class="col-lg-4 col-md-4">
				<div class="panel panel-primary">
        			<div class="panel-heading">TF-IDF</div>
              		<div class="panel-body" style="min-height: 500px; max-height: 500px;overflow-y: scroll;">''')

if tf_idf!=None:
	x = 0
	for result2 in tf_idf:
		x = x + 1
		link_string2 = "<a class='result_link' "
		link_string2 = link_string2 + " data-query="
		link_string2 = link_string2 + my_query
		link_string2 = link_string2 + " data-time="
		link_string2 = link_string2 + ctime()
		link_string2 = link_string2 + " data-path="
		link_string2 = link_string2 + str(result2['path'].encode("utf-8"))
		link_string2 = link_string2 + " data-technique="
		link_string2 = link_string2 + "TFIDF"
		link_string2 = link_string2 + " data-page="
		link_string2 = link_string2 + str(page_number_idf)
		link_string2 = link_string2 + " data-number="
		link_string2 = link_string2 + str(x)
		link_string2 = link_string2 + " data-title="
		link_string2 = link_string2 + str(result2['title'].encode("utf-8"))
		link_string2 = link_string2 + " href="
		link_string2 = link_string2 + result2['path'].encode("utf-8")
		link_string2 = link_string2 + ">"
		link_name2 	=  result2['title'].encode("utf-8")
		link_string2 = link_string2 + link_name2+"</a><br>\n"
		print link_string2
		print result2['path'].encode("utf-8")
		print "<br/>"
		print "<br/>"
		print result2.highlights("content").encode("utf-8")
		#print(result.highlights("content"))
		print "<br/>"
		print "<br/>"
print('''</div>
       			</div>
       				<div class="bs-docs-example">
                        <p style="margin-left:90px" class="demo demo3"></p>
                    </div>
		  	</div>
		  	<div class="col-lg-4 col-md-4">
				<div class="panel panel-primary">
        			<div class="panel-heading">TF</div>
              		<div class="panel-body" style="min-height: 500px; max-height: 500px;overflow-y: scroll;">''')

if tf!=None:
	x = 0
	for result3 in tf:
		x = x + 1
		link_string3 = "<a class='result_link' "
		link_string3 = link_string3 + "data-query="
		link_string3 = link_string3 + my_query
		link_string3 = link_string3 + " data-time="
		link_string3 = link_string3 + ctime()
		link_string3 = link_string3 + " data-path="
		link_string3 = link_string3 + str(result3['path'].encode("utf-8"))
		link_string3 = link_string3 + " data-technique="
		link_string3 = link_string3 + "TF"
		link_string3 = link_string3 + " data-page="
		link_string3 = link_string3 + str(page_number_tf)
		link_string3 = link_string3 + " data-number="
		link_string3 = link_string3 + str(x)
		link_string3 = link_string3 + " data-title="
		link_string3 = link_string3 + str(result3['title'].encode("utf-8"))
		link_string3 = link_string3 + " href="
		link_string3 = link_string3 + result3['path'].encode("utf-8")
		link_string3 = link_string3 + ">"
		link_name3 	=  result3['title'].encode("utf-8")
		link_string3 = link_string3 + link_name3+"</a><br>\n"
		print link_string3
		print (result3['path']).encode("utf-8")
		print "<br/>"
		print "<br/>"
		print result3.highlights("content").encode("utf-8")
		#print(result.highlights("content"))
		print "<br/>"
		print "<br/>"
print('''</div>
       			</div>
       			<div class="bs-docs-example">
                        <p style="margin-left:90px" class="demo demo4"></p>
                    </div>
		  	</div>
	  	</div>
	</div>
	 
	</body>
	<script>
		 $('.selectpicker').selectpicker();
	</script>''')

print ('''<script type="text/javascript">
                   a = $('.demo2').bootpag({
                   total:''') 

print len_bm25
print(''',
               	        page:''')
print int(page_number)
print(''',
                       maxVisible: 5
                    }).on('page', function(event, num)
                    {
                       	
                        document.getElementById("my_page_number").value = num;
                        document.getElementById("my_page_number_tf").value =''')
print int(page_number_tf)
print(''';
                        document.getElementById("my_page_number_idf").value =''')
print int(page_number_idf)
print(''';
                       	
                        document.getElementById("query").value=''')
if my_query!=None:
	print ("'"+my_query+"'")
print(''';
						document.getElementById("my_form").submit();

				    });
					
                    </script>''')

print(''' <script type="text/javascript">
                   a = $('.demo3').bootpag({
                   total:''') 

print len_tf_idf
print(''',
               	        page:''')
print int(page_number_idf)
print(''',
                       maxVisible: 5
                    }).on('page', function(event, num)
                    {
                       	
                        document.getElementById("my_page_number_idf").value = num;
                        document.getElementById("my_page_number").value =''')
print int(page_number)
print(''';
						document.getElementById("my_page_number_tf").value =''')
print int(page_number_tf)
print(''';
                        
                        document.getElementById("query").value=''')
if my_query!=None:
	print ("'"+my_query+"'")
print(''';
						document.getElementById("my_form").submit();

				    });
			
			</script>''')

print('''<script type="text/javascript">
                   a = $('.demo4').bootpag({
                   total:''') 

print len_tf
print(''',
               	        page:''')
print int(page_number_tf)
print(''',
                       maxVisible: 5
                    }).on('page', function(event, num)
                    {
                       	
                        document.getElementById("my_page_number_tf").value = num;
                        document.getElementById("my_page_number").value =''')
print int(page_number)
print(''';
						document.getElementById("my_page_number_idf").value =''')
print int(page_number_idf)
print(''';
                        
                       
                        document.getElementById("query").value=''')
if my_query!=None:
	print ("'"+my_query+"'")
print(''';
						document.getElementById("my_form").submit();

				    });
				
				</script>
					<script>
						$(function()
				            {
				                $('.result_link').click(function(){
				                    $.ajax({
				                        url: "create_log.py",
				                        type: "post",
				                        datatype:"json",
				                        data: {
				                        'query':($(this).data("query")),
										'time':($(this).data("time")),
										'path':($(this).data("path")),
										'technique':($(this).data("technique")),
										'page':(($(this).data("page"))),
										'number':($(this).data("number")),
										'title':($(this).data("title"))
				                        },
				                        success: function(response){
				                            alert(response.message);
				                            alert(response.keys);
				                        }
				                    });
				                });
				            });
					</script>
</html>


	''')

	
'''def tf_idf_search(query1):
	ix= index.open_dir("index")
	with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
		query=QueryParser("content",ix.schema).parse(query1)
		results = searcher.search_page(query,10,20)
		for result in results:
			print result
def term_frequency(query1):
	ix=index.open_dir("index")
	with ix.searcher(weighting=scoring.Frequency()) as searcher:
		query=QueryParser("content",ix.schema).parse(query1)
		results=searcher.search_page(query,10,20)
		for result in results:
			print result'''	

