import { Directive, ElementRef, HostListener, Input } from '@angular/core';

@Directive({
  selector: '[appHighlightRow]',
})
export class HighlightRowDirective {
  @Input()
  textColor: any = 'white';

  @Input()
  backgroundColor: any = 'gray';

  private originalTextColor: any = '';
  private originalBackgroundColor: any = '';

  constructor(private el: ElementRef) {}

  @HostListener('mouseenter') onMouseEnter() {
    this.originalTextColor = this.el.nativeElement.style.color;
    this.originalBackgroundColor = this.el.nativeElement.style.backgroundColor;

    this.el.nativeElement.style.backgroundColor = this.backgroundColor;
    this.el.nativeElement.style.color = this.textColor;
  }

  @HostListener('mouseleave') onMouseLeave() {
    this.el.nativeElement.style.backgroundColor = this.originalBackgroundColor;
    this.el.nativeElement.style.color = this.originalTextColor;
  }
}
