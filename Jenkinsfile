pipeline {
  agent any
  environment {
    file_name = "output.txt"
  }
  stages {
    stage('write file') {
      steps {
        writeFile(file: file_name, text: "output_text")
      }
    }
    stage('archive artifacts') {
      steps {
        archiveArtifacts file_name
      }
    }
  }
  post {
    always {
      // Always cleanup after the build.
      sh 'echo finished!'
    }
    success {
      cleanWs()
    }
  }
}
