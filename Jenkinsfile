pipeline {
  agent any
  stages {
    stage('lint') {
      steps {
        echo 'docker-compose up mysql'
        script {
          step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.yml', option: [$class: 'ExecuteCommandInsideContainer', command: 'mysql --version', index: 1, privilegedMode: false, service: 'mysql', workDir: ''], useCustomDockerComposeFile: true])
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
