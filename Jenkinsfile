pipeline {
  agent any
  stages {
    stage('parallel build') {
      steps {
        parallel(
          "01_hello_world": {
            build '01_hello_world'
          },
          "02_use_sh_step": {
            build '02_use_sh_step'
          },
          "03_write_file": {
            build(
              job: '03_write_file',
              parameters: [
                text(name: 'output.txt', value: 'hoge')
              ]
            )
          }
        )
      }
  }
  post {
    always {
      // Always cleanup after the build.
      sh 'echo finished!'
    }
  }
}
