pipeline {
  agent any
  stages {
    stage('lint') {
      steps {
        sh 'echo lint'
      }
    }
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
  post {
    always {
      // Always cleanup after the build.
      sh 'echo finished!'
    }
  }
}
