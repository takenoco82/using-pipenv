pipeline {
  agent any
  stages {
    stage('lint') {
      steps {
        sh 'docker-compose run --rm sandbox pipenv run lint'
      }
    }
    stage('test small') {
      steps {
        sh 'docker-compose run --rm ${SERVICE} pipenv run test_small'
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
