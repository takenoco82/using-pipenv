pipeline {
  agent any
  stages {
    stage('test small') {
      agent {
        docker {
          image 'python:3.7.0-alpine3.7'
        }

      }
      steps {
        sh 'python --version'
      }
    }
    stage('deploy') {
      steps {
        sh 'echo deploy'
      }
    }
  }
}
