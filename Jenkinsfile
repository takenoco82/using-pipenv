pipeline {
  agent none
  stages {
    stage('sandbox lint') {
      agent {
        // docker build -f Dockerfile --build-arg TESTING=true
        dockerfile {
          filename 'Dockerfile'
          additionalBuildArgs 'TESTING=true'
        }
      }
      steps {
        echo 'pipenv run lint'
        sh 'pipenv run lint'
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
