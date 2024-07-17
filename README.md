<h1>Attendance Automation Using Face Detection</h1>

<h2>Overview</h2>
<p>This project is a Face Recognition Software built using Python and Tkinter. It detects faces in real-time using a webcam, recognizes them if they are in the database, and records attendance automatically.</p>
<p>I developed this project as a mini project during my second year of college.</p>
<h2>Installation</h2>
<ol>
  <li><strong>Clone the Repository:</strong><br>
    <code>using git clone command</code><br>
    </li>
  
  <li><strong>Install Dependencies:</strong><br>
    <ul>
      <li>Ensure you have Python installed (preferably Python 3.x).</li>
      <li>Install necessary packages:<br>
        <code>pip install opencv-python pillow mysql-connector-python</code></li>
    </ul></li>
  
  <li><strong>Setup Database:</strong><br>
    <ul>
      <li>Create a MySQL database named <code>detailss</code>. I've used MySQL Workbench here.</li>
      <li>Create a table named <code>person</code>.</li>
      <li>Populate the table with user data.</li>
    </ul></li>
  
  <li><strong>Prepare Dataset:</strong><br>
    <ul>
      <li>Create a directory named <code>dataset</code>.</li>
    </ul></li>
  
  <li><strong>Training the Model:</strong><br>
    <ul>
      <li>Run <code>train.py</code> to train the face recognition model and generate <code>classifier.xml</code>.</li>
    </ul></li>
  
  <li><strong>Running the Application:</strong><br>
    <ul>
      <li>Execute <code>main.py</code> to start the Face Recognition Software.</li>
      <li>Click on the "DETECT" button to start face detection and recognition using the webcam.</li>
    </ul></li>
</ol>

<h2>Screenshots</h2>
<p><img src="Screenshot 2024-07-17 225947.png" alt="Screenshot 1"><br>
<em>Caption: Main Interface of the Face Recognition Software.</em></p>

<hr>

<p><strong>Note:</strong></p>
<ul>
  <li>Ensure you create an attendance.csv file to track and maintain attendance records.</li>
  <li>Make sure to replace database credentials like (<code>username</code>, <code>password</code>) in the code with your MySQL credentials.</li>
  <li>Ensure the Haar Cascade XML file (<code>haarcascade_frontalface_default.xml</code>) is accessible from the specified path.</li>
</ul>

<hr>

<p>Feel free to modify and enhance the software as per your requirements. If you have any issues or feedback, please contact <a href="mailto: satianmol9@gmail.com">satianmol9@gmail.com</a>.</p>
