node {
    //semi-nasty hack

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
        sh "pip install -r requirements.txt"
   }
   stage('BuildAndPackage'){
       echo 'Nothing to do for python!'
   }
   stage('Unit Test') {
    //sh "which python"
    //sh "python --version"
    def workspace = pwd()
    echo "ws:$workspace"
    sh "cd $workspace/wac; pytest unittests.py --junitxml=unittestsout.xml" // || true
    junit 'unittestsout.xml'
   }

   stage ('Integration Tests'){
       echo 'Weeeeee'

       //make web server not running then start
       sh "ps -ef | grep WAC_JENKINS_IT | grep -v grep | cut -d' ' -f4 | xargs --no-run-if-empty kill"
       sh "cd $workspace; python webserver.py --WAC_JENKINS_IT &"

       sleep 3

       //run integration tests
       sh "cd $workspace/wac; pytest integrationtests.py --junitxml=integrationtestsout.xml" // || true
       junit 'integrationtestsout.xml'

       //kill web server
       sh "ps -ef | grep WAC_JENKINS_IT | grep -v grep | cut -d' ' -f4 | xargs --no-run-if-empty kill"
   }
}