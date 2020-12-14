# Spot
### Requirements
 ### Setting solr 
  #### Download the latest release https://lucene.apache.org/solr/mirrors-solr-latest-redir.html and extract it .
     Navigate to bin folder and type - solr start
   this will start your solr server .
   #### create a core 
      solr create -c core_name
   #### Index your movies file to solr by -
   #### Win
     java -jar -Dc=core_name -Dauto exmaple\exampledocs\post.jar path_to_fle
   #### Linux
      post -c core_name path_to_file
 ### Setting Flask
 #### open terminal and type 
    pip install Flask
    pip install Flask-WTF
 #### run Flask server by opening a new terminal 
    python Hello.py (file is in the dir)
    
    
      
              
