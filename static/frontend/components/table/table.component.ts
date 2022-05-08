import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css'],
})
export class TableComponent implements OnInit {
  @Input()
  attributes: any[] = [];

  @Input()
  elements: any[] = [];

  @Output()
  edit: EventEmitter<any> = new EventEmitter();

  @Output()
  delete: EventEmitter<any> = new EventEmitter();

  title: string = 'Table';

  constructor() {}

  ngOnInit(): void {}

  emitEdit(i: any, v: any) {
    this.edit.emit({ index: i, value: { ...v } });
  }

  emitDelete(i: any, v: any) {
    this.delete.emit({ index: i, value: { ...v } });
  }

  sort(column: string): void {
    this.elements.sort((a: any, b: any) => {
      if (a[column] === undefined) {
        return -1;
      }

      if (a[column] < b[column]) {
        return -1;
      } else if (a[column] > b[column]) {
        return 1;
      } else {
        return 0;
      }
    });
  }
}
