from os import listdir	
from BeautifulSoup import BeautifulSoup	
from whoosh.writing import AsyncWriter	
import time
import sys				
from os.path import isfile,join			
from whoosh.index import create_in		
from whoosh.fields import *				
from whoosh.analysis import StemmingAnalyzer
from whoosh.analysis import StandardAnalyzer
from whoosh.analysis import SimpleAnalyzer
from whoosh.qparser import QueryParser
import whoosh.index as index


file_array = []		

def fetch_files(files_path):
	for i in listdir(files_path):
		if (not i.endswith('~')) and isfile(files_path+"/"+i):
			file_array.append(files_path+"/"+i)

def create_schema_indexing():
	global schema,ix,writer,stemming_stop_ix,stemming_ix,stop_ix,stop_writer,stemming_stop_writer,stemming_writer
	global stemming_stop,schema_st,stop_only
	stemming_stop = Schema(path=ID(stored=True,analyzer=StemmingAnalyzer()),title=TEXT(stored=True,analyzer=StemmingAnalyzer()),content=TEXT(analyzer=StemmingAnalyzer(),stored=True))
	stemming_only  = Schema(path=ID(stored=True,analyzer=StemmingAnalyzer(stoplist=None)),title=TEXT(stored=True,analyzer=StemmingAnalyzer(stoplist=None)),content=TEXT(analyzer=StemmingAnalyzer(stoplist=None),stored=True))
	stop_only   = Schema(path=ID(stored=True,analyzer=StandardAnalyzer()),title=TEXT(stored=True,analyzer=StandardAnalyzer()),content=TEXT(analyzer=StandardAnalyzer(),stored=True))
	schema      = Schema(path=ID(stored=True,analyzer=SimpleAnalyzer()),title=TEXT(stored=True,analyzer=SimpleAnalyzer()),content=TEXT(analyzer=SimpleAnalyzer(),stored=True))
	stemming_stop_ix=create_in("stemming_and_stop",stemming_stop)
	stemming_ix=create_in("stemming_without_stop",schema_st)
	stop_ix=create_in("stop_without_stemming",stop_only)
	ix = create_in("index", schema)

	stop_writer=stop_ix.writer()
	stemming_writer=stemming_ix.writer()
	stemming_stop_writer=stemmingstop_ix.writer()
	writer = ix.writer()


def index_data():
	for x in file_array:
		file_data=""
		with open(x) as file:
			file_data = file.read()
			file.close()
		try:
			soup = BeautifulSoup(file_data)
		except UnicodeEncodeError:
			pass
		except TypeError:
			soup = BeautifulSoup(file_data.decode('utf-8','ignore'))
		if soup.title is None:
			page_title = " "
		else:
			page_title = soup.title.string
		for skip in soup(["script", "style"]):
			skip.extract()
		data = soup.getText(separator=u' ')
		try:
			writer.add_document(title=unicode(page_title), path=unicode(x), content=unicode(data))
			stop_writer.add_document(title=unicode(page_title), path=unicode(x), content=unicode(data))
			stemming_writer.add_document(title=unicode(page_title), path=unicode(x), content=unicode(data))
			stemming_stop_writer.add_document(title=unicode(page_title), path=unicode(x), content=unicode(data))
		except UnicodeDecodeError:
			pass
		except UnicodeEncodeError:
			pass
	writer.commit()
	stop_writer.commit()
	stemming_writer.commit()
	stemming_stop_writer.commit()
	
def main():
	for x in range(24,27): fetch_files("Datasets/"+str(x))
	create_schema_indexing()
	index_data()
if __name__== "__main__":        
    main()
