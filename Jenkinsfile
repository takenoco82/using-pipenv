pipeline {
  agent none
  stages {
    stage('system property') {
      node('master') {
        System.setProperty("org.jenkinsci.plugins.durabletask.BourneShellScript.HEARTBEAT_CHECK_INTERVAL", "3800");
      }
    }
    stage('Node version') {
      agent {
        docker {
          image 'node:8-alpine'
        }
      }
      steps {
        sh 'ls'
        sh 'node --version'
      }
    }
    stage('sandbox lint') {
      agent {
        // docker build -f Dockerfile --build-arg TESTING=true
        dockerfile {
          filename 'Dockerfile'
          additionalBuildArgs '--build-arg TESTING=true'
          args '--no-cache'
        }
      }
      steps {
        sh 'pwd'
        sh 'ls'
        sh 'id'
        sh 'whoami'
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
