node {
    //semi-nasty hack
   def PYTHON_PATH = "/Library/Frameworks/Python.framework/Versions/2.7/"

   stage('Preparation') {
        echo 'Nuke the environment'
   }
   stage('Check Out') {
        echo 'Hello - about to start'
        git 'https://github.com/geod/CIDemo.git'
   }
   stage('Install Reqs'){
        def workspace = pwd()
        echo "ws:$workspace"
        sh "$PYTHON_PATH/bin/pip install -r requirements.txt"
   }
   stage('BuildAndPackage'){
       echo 'Nothing to do for python!'
   }
   stage('Unit Test') {
    //sh "which python"
    //sh "python --version"
    def workspace = pwd()
    echo "ws:$workspace"
    sh "cd $workspace; $PYTHON_PATH/bin/pytest unittests.py --junitxml=unittestsout.xml" // || true
    junit 'unittestsout.xml'
   }

   stage ('Integration Tests'){
       echo 'Weeeeee'
       sh "cd $workspace; $PYTHON_PATH/bin/pytest integrationtests.py --junitxml=integrationtestsout.xml" // || true
       junit 'integrationtestsout.xml'
   }
}