pipeline {
  agent none
  stages {
    stage('sandbox lint') {
      agent {
        // docker build -f Dockerfile --build-arg TESTING=true
        dockerfile {
          filename 'Dockerfile'
          additionalBuildArgs '--build-arg TESTING=true'
        }
      }
      steps {
        sh 'pipenv run pip freeze'
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
