echo 'hello there Ewan'
echo 'push test2'

stage('test'){
  script {
    py.test --junitxml results.xml tests.py
  }
}
