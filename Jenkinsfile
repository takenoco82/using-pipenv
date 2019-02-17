pipeline {
  agent any
  parameters {
    string(name: 'OUTPUT_TEXT', defaultValue: 'output.txt')
  }
  stages {
    stage('write file') {
      steps {
        writeFile(file: "output.txt", text: "${params.OUTPUT_TEXT}")
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
