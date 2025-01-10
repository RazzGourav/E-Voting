# Online E-Voting System

The project is an online voting system that uses facial recognition and aadhar number to authenticate voters and record their votes. The system ensures that each voter can only vote once and provides a user-friendly interface for casting votes.

# Tech Stack
1. Python: The core programming language used for developing the system.
2. OpenCV: Used for facial detection and recognition.
3. scikit-learn: Used for the K-Nearest Neighbors (KNN) classifier to recognize faces.
4. pickle: Used for saving and loading the trained model and label data.
5. win32com: Used for text-to-speech functionality.
6. CSV: Used for storing votes.


# Project Structure
How to Use
1. Setting Up the Environment
Install the required packages: pip install opencv-python scikit-learn numpy pywin32

3. Adding Faces
Run the add_faces.py script to add faces to the system: python add_faces.py
The script will capture images from your webcam and save the facial data in the data/ directory.
4. Voting
Run the give_vote.py script to start the voting process:

The system will use your webcam to recognize your face.

Once recognized, you can cast your vote by pressing the corresponding key:

Press 1 to vote for BJP
Press 2 to vote for Congress
Press 3 to vote for AAP
Press 4 to vote for NOTA
The system will confirm your vote and save it in the Votes.csv file.

4. Viewing Votes
Open the Votes.csv file to see the recorded votes.
Notes
Ensure that the data/ directory contains the faces_data.pkl and names.pkl files before running the give_vote.py script.
The system uses a KNN classifier with 5 neighbors for facial recognition.
The Votes.csv file will be created automatically if it does not exist.

