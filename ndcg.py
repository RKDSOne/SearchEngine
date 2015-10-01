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

form = cgi.FieldStorage()
my_query=form.getvalue('query')
my_selection = form.getvalue('selection')
relTf=form.getvalue('relTf')
relTfidf= form.getvalue('relTfidf')
relBm=form.getvalue('relBm')
count = form.getvalue('count')
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
			tf=searcher_tf.search_page(new_query_tf,int(page_number),10)
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
			tf_idf= searcher_idf.search_page(new_query_idf,int(page_number),10)

		ix_tf= index.open_dir("stop_without_stemming")
		searcher_tf= ix_tf.searcher(weighting=scoring.Frequency())
		if my_query!=None:
			new_query_tf= QueryParser("content",ix_tf.schema).parse(unicode(my_query))
			tf_counter = searcher_tf.search(new_query_tf)
			tf=searcher_tf.search_page(new_query_tf,int(page_number),10)
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
			  		<input type="hidden" name="relTf" id="relTf" value=''')
print  str(relTf)
print ('''>
					<input type="hidden" name="relTfidf" id="relTfidf" value=''')
print  str(relTfidf)
print ('''>
					<input type="hidden" name="relBm" id="relBm" value=''')
print  str(relBm)
print ('''>
					<input type="hidden" name="count" id="count" value=''')
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
	 			
				<a href="#" class="btn btn-primary" role="button" style=" margin-left:200px;" onclick="calculate_ndcg()">Calculate NDCG</a>
				<a href="searcher.py" class="btn btn-primary" role="button"  >Home</a>
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

if int(count)==10000:
	print "NDCG for BM25 is:"
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
			print "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"
			print('''
						<select class="bmRel">
							<option value="0">0</option>
							<option value="1">1</option>
							<option value="2">2</option>
							<option value="3">3</option>
							<option value="4">4</option>
						</select>
													
			''')

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
	print "NDCG for TF-IDF is:"
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
			print "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"
			print('''
						<select class="tfidfRel">
							<option value="0">0</option>
							<option value="1">1</option>
							<option value="2">2</option>
							<option value="3">3</option>
							<option value="4">4</option>
						</select>
													
			''')
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
	print "NDCG for TF is:"
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
			print "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"
			print('''
						<select class="tfRel">
							<option value="0">0</option>
							<option value="1">1</option>
							<option value="2">2</option>
							<option value="3">3</option>
							<option value="4">4</option>
						</select>
													
			''')
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

	                    function calculate_ndcg(){
	                   
	                	var x = document.getElementsByClassName("tfRel");
	                	var x1 = document.getElementsByClassName("tfidfRel");
	                	var x2 = document.getElementsByClassName("bmRel");
	                	var arr = [];
	                	var rel = [];
	                	if(x.length==0){
	                		document.getElementById("relTf").value = "0";
	                	}
	                	else{
	                		
	                		for(var i=0;i<x.length;i++){
	                			var selectedNode = x[i].options[x[i].selectedIndex];
			            		if(i==0){
			            			var k = 1.0*Number(selectedNode.value);
			            			arr.push(k);
			            		}
			            		else{
					        		var y = 1.0*Number(selectedNode.value);
					        		var pos = i+1;
					        		var demon = 1.0*Math.log(2);
					        		var nume = 1.0*Math.log(pos);
					        		var l = (nume/demon);
					        		var num = (y/l);
					        		arr.push(arr[i-1]+num);
			            		}
			            		rel.push(Number(selectedNode.value));
			            	}
			            	
			            	var init = arr[x.length-1];
			            	
			            	rel.sort(function(a, b){return b-a});
			            	
			            	arr = [];
			            	
			            	for(i=0;i<x.length;i++){
			            		if(i==0){
			            			var k = 1.0*(rel[i]);
			            			arr.push(k);
			            		}
			            		else{
					        		var y = Number(rel[i]);
					        		var pos = i+1;
					        		var demon = 1.0*Math.log(2);
					        		var nume = 1.0*Math.log(pos);
					        		var l = (nume/demon);
					        		var num = (y/l);
					        		arr.push(arr[i-1]+num);
			            		}
			            	}
			            	
			            	var ideal = arr[x.length-1];
			            	
			            	if(ideal!=0)
			            		document.getElementById("relTf").value = (init/ideal).toString();
			            	else
			            		 document.getElementById("relTf").value = "0";
			            	
	                	}
	                	
	                	/**for tfidf**/
	                	
	                	arr = [];
	                	rel = [];
	                	if(x1.length==0){
	                		document.getElementById("relTfidf").value = "0";
	                	}
	                	else{
	                		
	                		for(var i=0;i<x1.length;i++){
	                			var selectedNode = x1[i].options[x1[i].selectedIndex];
			            		if(i==0){
			            			var k = 1.0*Number(selectedNode.value);
			            			arr.push(k);
			            		}
			            		else{
					        		var y = 1.0*Number(selectedNode.value);
					        		var pos = i+1;
					        		var demon = 1.0*Math.log(2);
					        		var nume = 1.0*Math.log(pos);
					        		var l = (nume/demon);
					        		var num = (y/l);
					        		arr.push(arr[i-1]+num);
			            		}
			            		rel.push(Number(selectedNode.value));
			            	}
			            	
			            	var init = arr[x1.length-1];
			            	
			            	rel.sort(function(a, b){return b-a});
			            	
			            	arr = [];
			            	
			            	for(i=0;i<x1.length;i++){
			            		if(i==0){
			            			var k = 1.0*(rel[i]);
			            			arr.push(k);
			            		}
			            		else{
					        		var y = Number(rel[i]);
					        		var pos = i+1;
					        		var demon = 1.0*Math.log(2);
					        		var nume = 1.0*Math.log(pos);
					        		var l = (nume/demon);
					        		var num = (y/l);
					        		arr.push(arr[i-1]+num);
			            		}
			            	}
			            	
			            	var ideal = arr[x1.length-1];
			            	
			            	if(ideal!=0)
			            		document.getElementById("relTfidf").value = (init/ideal).toString();
			            	else
			            		 document.getElementById("relTfidf").value = "0";
			            	
	                	}
	                	/**for Bm25**/
	                	arr = [];
	                	rel = [];
	                	if(x2.length==0){
	                		document.getElementById("bmRel").value = "0";
	                	}
	                	else{
	                		
	                		for(var i=0;i<x2.length;i++){
	                			var selectedNode = x2[i].options[x2[i].selectedIndex];
			            		if(i==0){
			            			var k = 1.0*Number(selectedNode.value);
			            			arr.push(k);
			            		}
			            		else{
					        		var y = 1.0*Number(selectedNode.value);
					        		var pos = i+1;
					        		var demon = 1.0*Math.log(2);
					        		var nume = 1.0*Math.log(pos);
					        		var l = (nume/demon);
					        		var num = (y/l);
					        		arr.push(arr[i-1]+num);
			            		}
			            		rel.push(Number(selectedNode.value));
			            	}
			            	
			            	var init = arr[x2.length-1];
			            	
			            	rel.sort(function(a, b){return b-a});
			            	
			            	arr = [];
			            	
			            	for(i=0;i<x2.length;i++){
			            		if(i==0){
			            			var k = 1.0*(rel[i]);
			            			arr.push(k);
			            		}
			            		else{
					        		var y = Number(rel[i]);
					        		var pos = i+1;
					        		var demon = 1.0*Math.log(2);
					        		var nume = 1.0*Math.log(pos);
					        		var l = (nume/demon);
					        		var num = (y/l);
					        		arr.push(arr[i-1]+num);
			            		}
			            	}
			            	
			            	var ideal = arr[x2.length-1];
			            	
			            	if(ideal!=0)
			            		document.getElementById("relBm").value = (init/ideal).toString();
			            	else
			            		 document.getElementById("relBm").value = "0";
			            	
	                	}
	                	document.getElementById("count").value = "10000";
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

