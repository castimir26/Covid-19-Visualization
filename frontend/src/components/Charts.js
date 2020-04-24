import {Line} from 'react-chartjs'

class Charts extends React.Component {
  constructor(props) {
    super(props);
    this.state={
          chartData: {
            labels: this.props.date,
            datasets: [{
              data: Object.entries(this.props.historicalInfo.historicalInfo).map(date => {return(date[1]["4. close"])}),
            }]
          }
        }
  }
}
