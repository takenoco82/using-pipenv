pipeline {
  agent any
  stages {
    stage('lint') {
      steps {
        echo 'docker-compose up'
        script {
          step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.yml', option: [$class: 'StartAllServices'], useCustomDockerComposeFile: true])
        }
      }
    }
    stage('test small') {
      steps {
        echo 'test small'
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
