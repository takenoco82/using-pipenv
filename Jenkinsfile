pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        script {
          docker.build("sandbox:${env.BUILD_ID}")
        }
        sh "docker run --rm sandbox:${env.BUILD_ID} pipenv run pip freeze"
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
