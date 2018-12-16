pipeline {
  agent any
  stages {
    stage('lint') {
      steps {
        sh 'echo lint'
      }
    }
    stage('test small') {
      steps {
        sh 'echo test_small'
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
