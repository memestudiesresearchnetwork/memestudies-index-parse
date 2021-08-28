import json
import uuid
import csv

#create dictionary to store all index entries
index = {}
with open('Meme Studies Index .xlsx - Sheet1.csv', newline='', encoding='utf-8') as csvfile:
	reader = csv.DictReader(csvfile)
	#iterate through every line of csv file
	for row in reader:
		#create unique id for each entry
		id = uuid.uuid4().hex

		#create list of authors
		authors = [{'lastname': row['Author1 Last name'], 'firstname': row['Author1 First name']}]
		
		for i in range (2,6):
			author_to_add = 'Author' + str(i)
			if row[author_to_add + ' Last name']:
				authors.append({'lastname': row[author_to_add + ' Last name'], 'firstname': row[author_to_add + ' First name']})

		#create list of topics
		topics = [row['Topic1*'], row['Topic2*']]
		if row['Topic3']:
			topics.append(row['Topic3'])
		if row['Topic4']:
			topics.append(row['Topic4'])

		#create dictionary that holds all values for an entry
		index_entry = {'id': id, 'authors': authors, 'year': row['Year*'], 'article_name': row['Scholarly Article*'], 'resource_type': row['Resource Type'], 'book_bookname': row['Book'], 'book_bookeditor': row['Book edited by'], 'publisher': row['Publisher'], 'book_isbn': row['ISBN'], 'book_city': row['City (if book)'], 'journal_volume': row['Volume'], 'journal_number': row['Number'], 'journal_pages': row['Pages'], 'link': row['Link (Where Applicable)*'], 'subject': {'topics': topics, 'platform': row['Platform'], 'place': row['Place']}}
		
		#add entry dictionary to index dictionary
		index[id] = index_entry

with open("meme_studies_index.json", "w") as outfile:
    json.dump(index, outfile, indent=4, ensure_ascii=False)