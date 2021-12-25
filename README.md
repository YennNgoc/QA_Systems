# QA_Systems
QA_System based on Haystack Framework
<h1> Build Web Application </h1>
<p>Data: https://drive.google.com/drive/folders/1obM6_uT5BRliL97ZAWsh9ppb8V0_bGHd?usp=sharing </p>
<h3>Prepare Document Store</h3>
<ol>
  <li>Create file to save <code>viwwiki.json</code> data</li>
  <li>Run Elasticsearch Server (on Cloud or Docker) </li>
  <li>Run <code>prepare_data.py</code> </li> 
  <li>Run <code>document_store.py</code> => Write data to Elasticsearch Document Store </li>
  <li>Run Flask API <code>app.py</code> to test QA Systems</li>
</ol>
<h3>Prepare Reader Model </h3>
<ol> 
  <li>Train reader</code> data</li>
  <li>Save Reader checkpoint to <code>Flask/my_model</code></li>
  <li>Check Reader path at <code>Flask/app.py</code> before run Web apps</li>
</ol>
<h3>Run Flask API </h3>
<ol> 
  <li>Run <code>app.py</code> to test QA Systems</li>
  <li>Visit <code>localhost:8777</code> on the Browser to check if the system is up and running</li>
  <li>Navigate the <code>URL</code> to <code>localhost:8777/qna</code> for Q&A</li>
</ol>
<h3> Example </h3>
<img width="959" alt="ex" src="https://user-images.githubusercontent.com/50076309/147376973-8470d9e8-0867-4aea-b7d8-b1b03850fd7a.png">
<h1>System Architecture</h1>


![SystemArchitecture](https://user-images.githubusercontent.com/50076309/147376995-84eb8fd7-40bf-4bf4-b2c4-dbbdcb1323cd.jpg)
