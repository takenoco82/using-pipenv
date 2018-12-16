pipeline {
  agent {
    docker {
      image 'python:3.7.0-alpine3.7'
    }
  }
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
  }
  post {
    always {
      // Always cleanup after the build.
      sh 'echo finished!'
    }
  }
}
