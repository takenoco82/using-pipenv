pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        script {
          docker.build('sandbox:${env.BUILD_NUMBER}')
        }
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
