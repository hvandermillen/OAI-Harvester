from sickle import Sickle


def searchRecords(searchTerm, numResults):
    #harvard "worlds of change" digital collection
    woc = Sickle('https://api.lib.harvard.edu/oai/')

    # get a list of all records
    records = woc.ListRecords(metadataPrefix = 'mods', set='woc')

    #each element is an 2 element list: [name, url]
    results = []

    count = 0
    max = int(numResults) #how many results to return

    #display all records with a given searchterm
    for record in records:
        if (count >= max):
            break

        nameRaw = record.metadata.get('title')
        
        if isinstance(nameRaw, list): #if the record name is not nonetype
            name = ''.join(nameRaw[0]).lower()
            
            #check if the name contains the search term
            if isinstance(name, str) and searchTerm in name:
                #print the link to the record on harvard curiosity collections
                url = record.metadata.get("url")[-1]
                results.append([name,url])
                print(url)
                count += 1

    return results