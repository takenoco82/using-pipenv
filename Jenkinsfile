pipeline {
  agent none
  stages {
    stage('Python version') {
      agent {
        docker {
          image 'python:3.7.0-alpine3.7'
        }
      }
      steps {
        sh 'python --version'
      }
    }
    stage('Node version') {
      agent {
        docker {
          image 'node:8-alpine'
        }
      }
      steps {
        sh 'node --version'
      }
    }
  }
  post {
    always {
      node('master') {
        // Always cleanup after the build.
        sh 'echo finished!'
      }
    }
  }
}
