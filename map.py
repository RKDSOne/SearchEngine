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


relTf=None
relTfidf=None
relBm=None
count=None
len_bm25=0
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
i=0
form = cgi.FieldStorage()
my_query=form.getvalue('query')
my_selection = form.getvalue('selection')

relTf=form.getvalue('relTf')
relTfidf= form.getvalue('relTfidf')
relBm=form.getvalue('relBm')
count = form.getvalue('numQ')
if relBm == None:
	relBm="0"
if relTf==None:
	relTf="0"
if relTfidf==None:
	relTfidf="0"
if count==None:
	count="0"
if form.getvalue('my_page_number')!=None:
	page_number= int(form.getvalue('my_page_number'))
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
			tf_idf= searcher_idf.search_page(new_query_idf,int(page_number),10)

		ix_tf= index.open_dir("index")
		searcher_tf= ix_tf.searcher(weighting=scoring.Frequency())
		if my_query!=None:
			new_query_tf= QueryParser("content",ix_tf.schema).parse(unicode(my_query))
			tf_counter = searcher_tf.search(new_query_tf)
			tf=searcher_tf.search_page(new_query_tf,int(page_number),10)
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
			tf_idf= searcher_idf.search_page(new_query_idf,int(page_number),10)

		ix_tf= index.open_dir("stemming_and_stop")
		searcher_tf= ix_tf.searcher(weighting=scoring.Frequency())
		if my_query!=None:
			new_query_tf= QueryParser("content",ix_tf.schema).parse(unicode(my_query))
			tf_counter = searcher_tf.search(new_query_tf)
			tf=searcher_tf.search_page(new_query_tf,int(page_number),10)
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
			tf_idf= searcher_idf.search_page(new_query_idf,int(page_number),10)

		ix_tf= index.open_dir("stemming_without_stop")
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
			  	<div class="col-lg-6" style=" margin-left:170px;">
			  		<input type="hidden" name="my_page_number" id="my_page_number">
			  		<input type="hidden" name="relTf" id="relTf" value=''')
print  str(relTf)
print ('''>
					<input type="hidden" name="relTfidf" id="relTfidf" value=''')
print  str(relTfidf)
print ('''>
					<input type="hidden" name="relBm" id="relBm" value=''')
print  str(relBm)
print ('''>
					<input type="hidden" name="numQ" id="numQ" value=''')
print  str(count)
print ('''>
					<div class="input-group">
	  					<input type="text" id="query" name="query" class="form-control" placeholder="Search for...">
	  						<span class="input-group-btn">
	   					 		<button type="submit" value="Submit" class="btn btn-default">Go!
	   					 		</button>
	  						</span>
					</div><!-- /input-group -->
	 			</div><!-- /.col-lg-6 -->
	 			
				<a href="#" class="btn btn-primary" role="button" style=" margin-left:185px;" onclick="calculate_map()">Calculate MAP</a>
				<a href="#" class="btn btn-primary" role="button"  onclick="get_next_query()">Next</a>
				<a href="searcher.py" class="btn btn-primary" role="button"  >Home</a>
				<select name="selection" id="selection" class="form-control" style="max-width:13%;margin-top: -33px;">
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
if int(count)==10000:
	print "Mean Average Precision is:"
	print "<br/>" 
	print relBm
else:	
	if BM25!=None:
		for result in BM25:
			link_string = "<a href = "
			link_string = link_string + result['path'].encode("utf-8")
			link_string = link_string + ">"
			link_name 	= result['title'].encode("utf-8")
			link_string = link_string + link_name+"</a><br>\n"
			print link_string
			print result['path'].encode("utf-8")
			print('''<input  value="rel" class="bmRel" type="checkbox">''')
			print "<br/>"
			print "<br/>"
			print result.highlights("content").encode("utf-8")
			#print(result.highlights("content"))
			print "<br/>"
			print "<br/>"
if BM25!=None:
	if len(BM25)%10 == 0:
		len_bm25= len(BM25)/10
	else:
		len_bm25= len(BM25)/10 +1
print('''</div>
        		</div>
        			
                 	
				</div>
		  		
		  	<div class="col-lg-4 col-md-4">
				<div class="panel panel-primary">
        			<div class="panel-heading">TF-IDF</div>
              		<div class="panel-body" style="min-height: 500px; max-height: 500px;overflow-y: scroll;">''')

if int(count)==10000:
	print "Mean Average Precision is:"
	print "<br/>" 
	print relTfidf
else:
	if tf_idf!=None:
		for result2 in tf_idf:
			link_string2 = "<a href = "
			link_string2 = link_string2 + result2['path'].encode("utf-8")
			link_string2 = link_string2 + ">"
			link_name2 	=  result2['title'].encode("utf-8")
			link_string2 = link_string2 + link_name2+"</a><br>\n"
			print link_string2
			print result2['path'].encode("utf-8")
			print('''<input  value="rel" class="tfRel" type="checkbox">''')
			print "<br/>"
			print "<br/>"
			print result2.highlights("content").encode("utf-8")
			#print(result.highlights("content"))
			print "<br/>"
			print "<br/>"
print('''</div>
       			</div>
       			
		  	</div>
		  	<div class="col-lg-4 col-md-4">
				<div class="panel panel-primary">
        			<div class="panel-heading">TF</div>
              		<div class="panel-body" style="min-height: 500px; max-height: 500px;overflow-y: scroll;">''')

if int(count)==10000:
	print "Mean Average Precision is:"
	print "<br/>" 
	print relTf
else:
	if tf!=None:
		for result3 in tf:
			link_string3 = "<a href = "
			link_string3 = link_string3 + result3['path'].encode("utf-8")
			link_string3 = link_string3 + ">"
			link_name3 	=  result3['title'].encode("utf-8")
			link_string3 = link_string3 + link_name3+"</a><br>\n"
			print link_string3
			print (result3['path']).encode("utf-8")
			print('''<input  value="rel" class="tfidfRel" type="checkbox">''')
			print "<br/>"
			print "<br/>"
			print result3.highlights("content").encode("utf-8")
			#print(result.highlights("content"))
			print "<br/>"
			print "<br/>"
print('''</div>
       			</div>
		  	</div>
	  	</div>
	</div>
	 
	</body>
	<script>
		 $('.selectpicker').selectpicker();
	</script>
					
                    <script>
	                    function get_next_query(){
	                   
	                    var tfRel = document.getElementsByClassName("tfRel");
	                    var tfidfRel = document.getElementsByClassName("tfidfRel");
	                    var bmRel = document.getElementsByClassName("bmRel");
	                    var prevTf = document.getElementById("relTf").value;
	                    var prevTfidf = document.getElementById("relTfidf").value;
	                    var prevBm = document.getElementById("relBm").value;
	                    var prevCount = document.getElementById("numQ").value;
	                    /**for tf**/
	                    var arr=[];
	                    var rel = 0;
	                    var tot = 0;
	                    for (i = 0; i < tfRel.length; i++) {
	                        tot++;
	                        if(tfRel[i].checked==true){
	                            /*this means this is a relevant document*/
	                            rel++;
	                            rel = rel;
	                            tot = tot;
	                            var x = 1.0*rel;
	                            var y = 1.0*tot;
	                            arr.push(x/y);
	                        }
	                    }
	                    var cumFreq = 0.0;
	                    for (i=0;i<arr.length;i++){
	                        cumFreq += arr[i];
	                    }
	                    if(arr.length!=0){
	                        var newTf = (cumFreq/arr.length)
	                        document.getElementById("relTf").value = (Number(prevCount)*Number(prevTf) + newTf).toString();
	                    }
	                    else{
	                        document.getElementById("relTf").value = "0";
	                    }
	                    /**for tfidf**/
	                     arr=[];
	                    rel = 0;
	                    tot = 0;
	                    for (i = 0; i < tfidfRel.length; i++) {
	                        tot++;
	                        if(tfidfRel[i].checked==true){
	                            /*this means this is a relevant document*/
	                            rel++;
	                            rel = rel;
	                            tot = tot;
	                            var x = 1.0*rel;
	                            var y = 1.0*tot;
	                            arr.push(x/y);
	                        }
	                    }
	                    var cumFreq = 0.0;
	                    for (i=0;i<arr.length;i++){
	                        cumFreq += arr[i];
	                    }
	                    if(arr.length!=0){
	                        var newTfidf = (cumFreq/arr.length);
	                        document.getElementById("relTfidf").value = (Number(prevCount)*Number(prevTfidf) + newTfidf).toString();
	                    }
	                    else{
	                        document.getElementById("relTfidf").value = "0";
	                    }
	                    /**for bm25**/
	                    arr=[];
	                    rel = 0;
	                   	tot = 0;
	                    for (i = 0; i < bmRel.length; i++) {
	                        tot++;
	                        if(bmRel[i].checked==true){
	                            /*this means this is a relevant document*/
	                            rel++;
	                            rel = rel;
	                            tot = tot;
	                            var x = 1.0*rel;
	                            var y = 1.0*tot;
	                            arr.push(x/y);
	                        }
	                    }
	                    var cumFreq = 0.0;
	                    for (i=0;i<arr.length;i++){
	                        cumFreq += arr[i];
	                    }
	                    if(arr.length!=0){
	                        var newBm = (cumFreq/arr.length);
	                        document.getElementById("relBm").value = (Number(prevCount)*Number(prevBm) + newBm).toString();
	                    }
	                    else{
	                        document.getElementById("relBm").value = "0";
	                    }
	                    document.getElementById("numQ").value = (Number(prevCount)+1).toString();
	                    document.getElementById("my_form").submit();
	                }
	                
	               
	                
            	</script>
            	<script>
            		 function calculate_map(){
	                	var prevTf = document.getElementById("relTf").value;
	                    var prevTfidf = document.getElementById("relTfidf").value;
	                    var prevBm = document.getElementById("relBm").value;
	                    var prevCount = document.getElementById("numQ").value;
	                    document.getElementById("relTf").value = (Number(prevTf)/Number(prevCount)).toString()
	                    document.getElementById("relTfidf").value = (Number(prevTfidf)/Number(prevCount)).toString()
	                    document.getElementById("relBm").value = (Number(prevBm)/Number(prevCount)).toString()
	                    document.getElementById("numQ").value = "10000";
	                    document.getElementById("my_form").submit();
	                }
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

